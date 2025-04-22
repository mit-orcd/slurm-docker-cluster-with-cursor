import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def generate_docker_compose(
    num_compute_nodes: int = 4,
    num_login_nodes: int = 1,
    num_ldap_nodes: int = 1,
    num_service_nodes: int = 1,
    login_mem_limit: int = 24,
    login_prefix: str = "login",
    output_file: str = "docker-compose.yml"
) -> None:
    """
    Generate a Docker Compose file with a specified number of compute nodes, login nodes, LDAP nodes, and service nodes.
    
    Args:
        num_compute_nodes (int): Number of compute nodes to generate (default: 4)
        num_login_nodes (int): Number of login nodes to generate (default: 1)
        num_ldap_nodes (int): Number of LDAP nodes to generate (default: 1)
        num_service_nodes (int): Number of service nodes to generate (default: 1)
        login_mem_limit (int): Memory limit in GB for each login node (default: 24)
        login_prefix (str): Prefix to use for login node names (default: "login")
        output_file (str): Path to the output file (default: docker-compose.yml)
    """
    # Validate minimum number of nodes
    if num_compute_nodes < 2:
        raise ValueError("Number of compute nodes must be at least 2")
    if num_login_nodes < 1:
        raise ValueError("Number of login nodes must be at least 1")
    if num_ldap_nodes < 1:
        raise ValueError("Number of LDAP nodes must be at least 1")
    if num_service_nodes < 1:
        raise ValueError("Number of service nodes must be at least 1")
    
    # Set up Jinja2 environment
    template_dir = Path(__file__).parent
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template("docker-compose.j2")
    
    # Render template with the specified parameters
    rendered = template.render(
        num_compute_nodes=num_compute_nodes,
        num_login_nodes=num_login_nodes,
        num_ldap_nodes=num_ldap_nodes,
        num_service_nodes=num_service_nodes,
        login_mem_limit=login_mem_limit,
        login_prefix=login_prefix
    )
    
    # Write the rendered template to the output file
    with open(output_file, "w") as f:
        f.write(rendered)
    
    print(f"Generated Docker Compose file with {num_compute_nodes} compute nodes, {num_login_nodes} login nodes, {num_ldap_nodes} LDAP nodes, {num_service_nodes} service nodes, and {login_mem_limit}GB login memory at {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate a Docker Compose file with configurable number of compute nodes, login nodes, LDAP nodes, and service nodes")
    parser.add_argument(
        "-n", "--num-nodes",
        type=int,
        default=4,
        help="Number of compute nodes to generate (minimum: 2, default: 4)"
    )
    parser.add_argument(
        "-l", "--num-login",
        type=int,
        default=1,
        help="Number of login nodes to generate (minimum: 1, default: 1)"
    )
    parser.add_argument(
        "--num-ldap",
        type=int,
        default=1,
        help="Number of LDAP nodes to generate (minimum: 1, default: 1)"
    )
    parser.add_argument(
        "--num-service",
        type=int,
        default=1,
        help="Number of service nodes to generate (minimum: 1, default: 1)"
    )
    parser.add_argument(
        "-m", "--login-mem",
        type=int,
        default=24,
        help="Memory limit in GB for each login node (default: 24)"
    )
    parser.add_argument(
        "-p", "--login-prefix",
        default="login",
        help="Prefix to use for login node names (default: login)"
    )
    parser.add_argument(
        "-o", "--output",
        default="docker-compose.yml",
        help="Output file path (default: docker-compose.yml)"
    )
    
    args = parser.parse_args()
    generate_docker_compose(args.num_nodes, args.num_login, args.num_ldap, args.num_service, args.login_mem, args.login_prefix, args.output)

if __name__ == "__main__":
    main() 