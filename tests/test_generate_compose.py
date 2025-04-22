import pytest
from src.generate_compose import generate_docker_compose
import yaml
import os
from pathlib import Path

def test_generate_docker_compose(tmp_path):
    # Create a temporary output file
    output_file = tmp_path / "docker-compose.yml"
    
    # Generate a compose file with 4 nodes and default memory (24GB)
    generate_docker_compose(4, 24, str(output_file))
    
    # Verify the file exists
    assert os.path.exists(output_file)
    
    # Load and verify the YAML content
    with open(output_file, 'r') as f:
        config = yaml.safe_load(f)
        
        # Check services
        assert 'services' in config
        assert 'login' in config['services']
        assert config['services']['login']['mem_limit'] == '24G'
        assert config['services']['login']['mem_reservation'] == '24G'
        assert 'c001' in config['services']
        assert 'c004' in config['services']
        assert 'c005' not in config['services']  # Should not exist
        
        # Check volumes
        assert 'volumes' in config
        assert 'c001_slurmd_state' in config['volumes']
        assert 'c004_slurmd_state' in config['volumes']
        assert 'c005_slurmd_state' not in config['volumes']  # Should not exist
        
        # Check networks
        assert 'networks' in config
        assert 'compute' in config['networks']

def test_generate_docker_compose_custom_nodes(tmp_path):
    # Create a temporary output file
    output_file = tmp_path / "docker-compose.yml"
    
    # Generate a compose file with 2 nodes
    generate_docker_compose(2, 24, str(output_file))
    
    # Load and verify the YAML content
    with open(output_file, 'r') as f:
        config = yaml.safe_load(f)
        
        # Check services
        assert 'c001' in config['services']
        assert 'c002' in config['services']
        assert 'c003' not in config['services']  # Should not exist
        
        # Check volumes
        assert 'c001_slurmd_state' in config['volumes']
        assert 'c002_slurmd_state' in config['volumes']
        assert 'c003_slurmd_state' not in config['volumes']  # Should not exist

def test_generate_docker_compose_custom_memory(tmp_path):
    # Create a temporary output file
    output_file = tmp_path / "docker-compose.yml"
    
    # Generate a compose file with custom memory limit
    generate_docker_compose(4, 32, str(output_file))
    
    # Load and verify the YAML content
    with open(output_file, 'r') as f:
        config = yaml.safe_load(f)
        
        # Check login service memory settings
        assert config['services']['login']['mem_limit'] == '32G'
        assert config['services']['login']['mem_reservation'] == '32G' 