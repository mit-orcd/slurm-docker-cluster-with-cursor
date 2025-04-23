#!/bin/bash

# Configuration
NUM_COMPUTE_NODES=4
NUM_LOGIN_NODES=1
NUM_LDAP_NODES=1
NUM_SERVICE_NODES=1
LOGIN_PREFIX="login"
LOGIN_MEM_LIMIT=24

# Create network namespaces
create_network() {
    local net_name=$1
    ip netns add $net_name
    ip netns exec $net_name ip link set lo up
}

# Create networks
create_network compute
create_network inband
create_network ib

# Create volume directories
mkdir -p volumes/home
mkdir -p volumes/etc_slurm
mkdir -p volumes/etc_munge
mkdir -p volumes/root_ssh
mkdir -p volumes/slurmctld_state
mkdir -p volumes/slurmdbd_state

# Copy SSH keys to volume
cp -r volume_inputs/root_ssh/* volumes/root_ssh/
chmod 700 volumes/root_ssh
chmod 600 volumes/root_ssh/*

# Function to start a container
start_container() {
    local name=$1
    local hostname=$2
    local networks=$3
    local volumes=$4
    local mem_limit=$5
    local port=$6

    # Build container if not exists
    if [ ! -f "$name.sif" ]; then
        apptainer build $name.sif Apptainer.def
    fi

    # Prepare network namespace
    for net in $networks; do
        ip netns exec $net ip link add veth-$name type veth peer name veth-$name-ns
        ip netns exec $net ip link set veth-$name-ns netns $name
        ip netns exec $net ip link set veth-$name up
        ip netns exec $name ip link set veth-$name-ns up
        ip netns exec $name ip addr add 10.0.0.${name//[^0-9]/}/24 dev veth-$name-ns
    done

    # Start container
    apptainer instance start \
        --net --network-args "name=$name" \
        --bind "$volumes" \
        ${mem_limit:+--memory ${mem_limit}G} \
        ${port:+--port $port:22} \
        $name.sif $name

    # Set hostname
    apptainer exec instance://$name hostname $hostname
}

# Start LDAP nodes
for i in $(seq 1 $NUM_LDAP_NODES); do
    name="ldap$(printf "%03d" $i)"
    start_container $name $name "compute inband ib" \
        "volumes/home:/home,volumes/etc_slurm:/etc/slurm,volumes/etc_munge:/etc/munge,volumes/root_ssh:/root/.ssh"
done

# Start login nodes
for i in $(seq 1 $NUM_LOGIN_NODES); do
    name="${LOGIN_PREFIX}$(printf "%03d" $i)"
    port=$((6321 + i))
    start_container $name $name "compute inband ib" \
        "volumes/home:/home,volumes/etc_slurm:/etc/slurm,volumes/etc_munge:/etc/munge,volumes/root_ssh:/root/.ssh" \
        $LOGIN_MEM_LIMIT $port
done

# Start compute nodes
for i in $(seq 1 $NUM_COMPUTE_NODES); do
    name="node$(printf "%04d" $i)"
    start_container $name $name "compute inband ib" \
        "volumes/home:/home,volumes/etc_slurm:/etc/slurm,volumes/etc_munge:/etc/munge,volumes/root_ssh:/root/.ssh"
done

# Start service nodes
for i in $(seq 1 $NUM_SERVICE_NODES); do
    name="service$(printf "%04d" $i)"
    start_container $name $name "compute inband ib" \
        "volumes/home:/home,volumes/etc_slurm:/etc/slurm,volumes/etc_munge:/etc/munge,volumes/root_ssh:/root/.ssh"
done

# Start Slurm controller
start_container slurmctld slurmctld "compute inband ib" \
    "volumes/home:/home,volumes/etc_slurm:/etc/slurm,volumes/etc_munge:/etc/munge,volumes/root_ssh:/root/.ssh,volumes/slurmctld_state:/var/spool/slurmctld"

# Start Slurm database
start_container slurmdbd slurmdbd "compute inband ib" \
    "volumes/home:/home,volumes/etc_slurm:/etc/slurm,volumes/etc_munge:/etc/munge,volumes/root_ssh:/root/.ssh,volumes/slurmdbd_state:/var/spool/slurmdbd"

# Function to stop containers and clean up
cleanup() {
    echo "Cleaning up..."
    
    # Stop all containers
    for container in $(apptainer instance list | awk 'NR>1 {print $1}'); do
        apptainer instance stop $container
    done
    
    # Remove network namespaces
    for net in compute inband ib; do
        ip netns delete $net 2>/dev/null || true
    done
    
    # Remove SIF files
    rm -f *.sif
    
    echo "Cleanup complete"
}

# Set up trap for cleanup
trap cleanup EXIT

# Keep script running
echo "Cluster is running. Press Ctrl+C to stop."
while true; do
    sleep 1
done 