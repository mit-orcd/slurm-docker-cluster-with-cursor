# Docker Compose Generator

A Python library for programmatically generating Docker Compose configurations for Slurm clusters.

## Features

- Create Docker Compose configurations programmatically
- Support for common Docker Compose service configurations
- Generate YAML files ready for use with Docker Compose
- Type-safe service configuration using Python dataclasses
- Configurable number of compute nodes
- Adjustable login node memory limits
- Jinja2 templating for flexible configuration generation
- Example configurations with detailed documentation

## Project Structure

```
docker_compose_generator/
├── src/
│   ├── __init__.py
│   ├── docker-compose.j2
│   ├── docker_compose_generator.py
│   └── generate_compose.py
├── tests/
│   ├── __init__.py
│   ├── test_docker_compose_generator.py
│   └── test_generate_compose.py
├── examples/
│   ├── README.md
│   └── example_basic_cluster/
│       ├── Dockerfile
│       ├── README.md
│       └── generate_example.py
├── .gitignore
├── LICENSE
├── PROMPT_HISTORY.md
├── README.md
├── requirements.txt
└── setup.py
```

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from src.docker_compose_generator import DockerComposeGenerator, Service

# Create a generator instance
generator = DockerComposeGenerator()

# Create a service
web_service = Service(
    name="web",
    image="nginx:latest",
    ports=["80:80"],
    environment={"DEBUG": "true"},
    volumes=["./app:/app"]
)

# Add the service to the generator
generator.add_service(web_service)

# Generate and save the configuration
generator.save_to_file("docker-compose.yml")
```

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

- `PROMPT_HISTORY.md`: Documents the evolution of the project
- Example READMEs: Detailed usage instructions for each example
- Inline code documentation

## License

MIT License 