# Docker Compose Generator Examples

This directory contains example scripts demonstrating how to use the Docker Compose Generator.

## Example Script: generate_example.py

This script demonstrates how to generate a Docker Compose file for a Slurm cluster with configurable compute nodes and login memory.

### Usage

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
3. Stop the cluster:
   ```bash
   docker-compose -f example-docker-compose.yml down
   ```

### Notes

- The generated file is meant to be a starting point and may need customization for your specific needs
- Make sure Docker and Docker Compose are installed and running
- The script requires Python 3.8 or later 