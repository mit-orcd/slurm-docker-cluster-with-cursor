#!/usr/bin/env python3
"""
Example driver script for the Docker Compose Generator.

This script demonstrates how to use the Docker Compose Generator to create
a Docker Compose file with configurable compute nodes and login memory.
"""

import argparse
import sys
from pathlib import Path

# Add the parent directory to the Python path to import the package
sys.path.append(str(Path(__file__).parent.parent))

from src.generate_compose import generate_docker_compose

def main():
    parser = argparse.ArgumentParser(
        description="Generate an example Docker Compose file for a Slurm cluster"
    )
    parser.add_argument(
        "-n", "--num-nodes",
        type=int,
        default=4,
        help="Number of compute nodes to generate (default: 4)"
    )
    parser.add_argument(
        "-m", "--login-mem",
        type=int,
        default=24,
        help="Memory limit in GB for the login node (default: 24)"
    )
    parser.add_argument(
        "-o", "--output",
        default="example-docker-compose.yml",
        help="Output file path (default: example-docker-compose.yml)"
    )
    
    args = parser.parse_args()
    
    # Generate the Docker Compose file
    generate_docker_compose(
        num_compute_nodes=args.num_nodes,
        login_mem_limit=args.login_mem,
        output_file=args.output
    )
    
    print(f"\nExample Docker Compose file generated successfully!")
    print(f"Number of compute nodes: {args.num_nodes}")
    print(f"Login node memory: {args.login_mem}GB")
    print(f"Output file: {args.output}")
    print("\nTo use this configuration:")
    print("1. Review the generated file")
    print("2. Run 'docker-compose -f {args.output} up -d' to start the cluster")
    print("3. Run 'docker-compose -f {args.output} down' to stop the cluster")

if __name__ == "__main__":
    main() 