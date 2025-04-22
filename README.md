# Docker Compose Generator

A Python library for programmatically generating Docker Compose configurations.

## Features

- Create Docker Compose configurations programmatically
- Support for common Docker Compose service configurations
- Generate YAML files ready for use with Docker Compose
- Type-safe service configuration using Python dataclasses

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

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

## Development

To run tests:
```bash
pytest tests/
```

## License

MIT License 