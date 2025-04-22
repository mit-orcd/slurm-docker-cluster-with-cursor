# Basic Slurm Cluster Example

This example demonstrates how to generate a basic Slurm cluster configuration with configurable compute nodes and login memory.

## Files

- `generate_example.py`: Script to generate the Docker Compose configuration
- `Dockerfile`: Base image configuration for the Slurm nodes

## Usage

```bash
# Generate with default settings (4 nodes, 24GB login memory)
python generate_example.py

# Generate with custom number of nodes
python generate_example.py -n 8

# Generate with custom login memory
python generate_example.py -m 32

# Generate with custom output file
python generate_example.py -o my-cluster.yml

# Combine options
python generate_example.py -n 8 -m 32 -o large-cluster.yml
```

### Default Settings

- Number of compute nodes: 4
- Login node memory: 24GB
- Output file: example-docker-compose.yml

### Generated Configuration

The script generates a Docker Compose file with:
- A login node with configurable memory
- The specified number of compute nodes
- Required volumes for Slurm
- A compute network for node communication

### Using the Generated Configuration

1. Review the generated Docker Compose file
2. Start the cluster:
   ```bash
   docker-compose -f example-docker-compose.yml up -d
   ```
   This will automatically build the required Docker image using the Dockerfile in the current directory.
3. Stop the cluster:
   ```bash
   docker-compose -f example-docker-compose.yml down
   ```

### Notes

- The generated file is meant to be a starting point and may need customization for your specific needs
- Make sure Docker and Docker Compose are installed and running
- The script requires Python 3.8 or later
- The Dockerfile in this directory provides the base configuration for all nodes in the cluster
- Docker Compose will automatically build the required image using the local Dockerfile 