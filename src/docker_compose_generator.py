import yaml
from typing import Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Service:
    """Represents a Docker service configuration."""
    name: str
    image: str
    ports: Optional[List[str]] = None
    environment: Optional[Dict[str, str]] = None
    volumes: Optional[List[str]] = None
    depends_on: Optional[List[str]] = None

class DockerComposeGenerator:
    """A class to generate Docker Compose configurations."""
    
    def __init__(self, version: str = "3.8"):
        self.version = version
        self.services: Dict[str, Service] = {}
    
    def add_service(self, service: Service) -> None:
        """Add a service to the Docker Compose configuration."""
        self.services[service.name] = service
    
    def generate_compose(self) -> Dict:
        """Generate the Docker Compose configuration as a dictionary."""
        compose_dict = {
            "version": self.version,
            "services": {}
        }
        
        for service_name, service in self.services.items():
            service_config = {
                "image": service.image
            }
            
            if service.ports:
                service_config["ports"] = service.ports
            if service.environment:
                service_config["environment"] = service.environment
            if service.volumes:
                service_config["volumes"] = service.volumes
            if service.depends_on:
                service_config["depends_on"] = service.depends_on
                
            compose_dict["services"][service_name] = service_config
        
        return compose_dict
    
    def save_to_file(self, filepath: str) -> None:
        """Save the Docker Compose configuration to a YAML file."""
        compose_dict = self.generate_compose()
        with open(filepath, 'w') as f:
            yaml.dump(compose_dict, f, default_flow_style=False) 