# Docker Compose Generator Examples

This directory contains various example configurations demonstrating how to use the Docker Compose Generator.

## Available Examples

### Basic Cluster (`example_basic_cluster/`)

A basic Slurm cluster configuration with configurable compute nodes and login memory.

Features:
- Configurable number of compute nodes
- Adjustable login node memory
- Basic Slurm setup with required volumes
- Simple network configuration

See the [example_basic_cluster README](example_basic_cluster/README.md) for detailed usage instructions.

## Running Examples

1. Navigate to the example directory:
   ```bash
   cd examples/example_basic_cluster
   ```

2. Install the package in development mode:
   ```bash
   pip install -e ../..
   ```

3. Run the example script:
   ```bash
   python generate_example.py
   ```

## Creating New Examples

To create a new example:
1. Create a new directory under `examples/`
2. Include a README.md with usage instructions
3. Create example scripts that demonstrate specific use cases
4. Update this README to document the new example 