import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def generate_docker_compose(
    num_compute_nodes: int = 4,
    login_mem_limit: int = 24,
    output_file: str = "docker-compose.yml"
) -> None:
    """
    Generate a Docker Compose file with a specified number of compute nodes.
    
    Args:
        num_compute_nodes (int): Number of compute nodes to generate (default: 4)
        login_mem_limit (int): Memory limit in GB for the login node (default: 24)
        output_file (str): Path to the output file (default: docker-compose.yml)
    """
    # Set up Jinja2 environment
    template_dir = Path(__file__).parent
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template("docker-compose.j2")
    
    # Render template with the specified parameters
    rendered = template.render(
        num_compute_nodes=num_compute_nodes,
        login_mem_limit=login_mem_limit
    )
    
    # Write the rendered template to the output file
    with open(output_file, "w") as f:
        f.write(rendered)
    
    print(f"Generated Docker Compose file with {num_compute_nodes} compute nodes and {login_mem_limit}GB login memory at {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate a Docker Compose file with configurable number of compute nodes")
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
        default="docker-compose.yml",
        help="Output file path (default: docker-compose.yml)"
    )
    
    args = parser.parse_args()
    generate_docker_compose(args.num_nodes, args.login_mem, args.output)

if __name__ == "__main__":
    main() 