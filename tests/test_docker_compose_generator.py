import pytest
from src.docker_compose_generator import DockerComposeGenerator, Service
import yaml
import os

def test_add_service():
    generator = DockerComposeGenerator()
    service = Service(
        name="web",
        image="nginx:latest",
        ports=["80:80"],
        environment={"DEBUG": "true"}
    )
    generator.add_service(service)
    assert "web" in generator.services
    assert generator.services["web"].image == "nginx:latest"

def test_generate_compose():
    generator = DockerComposeGenerator()
    service = Service(
        name="web",
        image="nginx:latest",
        ports=["80:80"]
    )
    generator.add_service(service)
    compose_dict = generator.generate_compose()
    
    assert compose_dict["version"] == "3.8"
    assert "web" in compose_dict["services"]
    assert compose_dict["services"]["web"]["image"] == "nginx:latest"
    assert compose_dict["services"]["web"]["ports"] == ["80:80"]

def test_save_to_file(tmp_path):
    generator = DockerComposeGenerator()
    service = Service(
        name="web",
        image="nginx:latest",
        ports=["80:80"]
    )
    generator.add_service(service)
    
    filepath = tmp_path / "docker-compose.yml"
    generator.save_to_file(str(filepath))
    
    assert os.path.exists(filepath)
    with open(filepath, 'r') as f:
        saved_config = yaml.safe_load(f)
        assert saved_config["version"] == "3.8"
        assert "web" in saved_config["services"] 