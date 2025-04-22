# Docker Compose Generator

A Python library for programmatically generating Docker Compose configurations for Slurm clusters. This tool allows you to create complex HPC (High Performance Computing) cluster configurations with multiple types of nodes, networks, and services.

## Key Features

- **Flexible Node Configuration**
  - Configurable number of compute nodes (minimum 2)
  - Multiple login nodes with adjustable memory limits
  - LDAP nodes for authentication and directory services
  - Service nodes for additional utilities
  - Dedicated Slurm controller and database nodes

- **Network Configuration**
  - Multiple internal networks (compute, inband, ib)
  - Hostname aliases for network-specific addressing
  - Consistent network configuration across all node types

- **Volume Management**
  - Shared home directories
  - Configuration volumes for Slurm and Munge
  - State volumes for Slurm services
  - Persistent storage for each node type

- **Customization Options**
  - Adjustable login node memory limits
  - Configurable login node prefix
  - Flexible number of nodes for each type
  - Jinja2 templating for complex configurations

## Repository Structure

```
docker_compose_generator/
├── src/                           # Source code directory
│   ├── __init__.py               # Package initialization
│   ├── docker-compose.j2         # Jinja2 template for Docker Compose
│   ├── docker_compose_generator.py # Core generator class
│   └── generate_compose.py       # Command-line interface
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── test_docker_compose_generator.py
│   └── test_generate_compose.py
├── examples/                     # Example configurations
│   ├── README.md
│   └── example_basic_cluster/    # Basic cluster example
│       ├── Dockerfile           # Base image configuration
│       ├── README.md           # Example-specific documentation
│       └── generate_example.py # Example generation script
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
├── PROMPT_HISTORY.md           # Project evolution documentation
├── README.md                   # This file
├── requirements.txt            # Python dependencies
└── setup.py                    # Package setup configuration
```

## Core Components

### 1. Jinja2 Template (`docker-compose.j2`)
- Defines the structure of the Docker Compose configuration
- Supports multiple node types with consistent configuration
- Implements network and volume configurations
- Uses loops for generating multiple instances of each node type

### 2. Generator Class (`docker_compose_generator.py`)
- Core functionality for generating Docker Compose configurations
- Type-safe service configuration using Python dataclasses
- Support for common Docker Compose service configurations
- YAML generation and file output capabilities

### 3. Command-line Interface (`generate_compose.py`)
- User-friendly interface for generating configurations
- Command-line arguments for all configurable options
- Validation of input parameters
- Helpful error messages and documentation

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mit-orcd/slurm-docker-cluster-with-cursor.git
cd slurm-docker-cluster-with-cursor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Generate a basic cluster configuration:
```bash
python -m src.generate_compose -n 4 -l 2 --num-ldap 1 --num-service 2
```

This creates a cluster with:
- 4 compute nodes
- 2 login nodes
- 1 LDAP node
- 2 service nodes
- 1 Slurm controller node
- 1 Slurm database node

### Command-line Options

- `-n, --num-nodes`: Number of compute nodes (minimum: 2, default: 4)
- `-l, --num-login`: Number of login nodes (minimum: 1, default: 1)
- `--num-ldap`: Number of LDAP nodes (minimum: 1, default: 1)
- `--num-service`: Number of service nodes (minimum: 1, default: 1)
- `-m, --login-mem`: Memory limit in GB for login nodes (default: 24)
- `-p, --login-prefix`: Prefix for login node names (default: "login")
- `-o, --output`: Output file path (default: "docker-compose.yml")

### Example Configurations

The project includes example configurations in the `examples` directory:

- `example_basic_cluster/`: A basic Slurm cluster configuration
  - Configurable number of compute nodes
  - Adjustable login node memory
  - Includes Dockerfile for node configuration

To use the example:
```bash
cd examples/example_basic_cluster
python generate_example.py
```

## Development

### Running Tests

```bash
# Install in development mode
pip install -e .

# Run tests
pytest tests/
```

### Adding New Features

1. Create new Jinja2 templates in `src/`
2. Add corresponding Python modules
3. Update tests
4. Add example configurations if applicable

## Documentation

- `PROMPT_HISTORY.md`: Documents the evolution of the project and all changes made
- Example READMEs: Detailed usage instructions for each example
- Inline code documentation
- This README: Overview of the project and its components

## License

MIT License - See LICENSE file for details 