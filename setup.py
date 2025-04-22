from setuptools import setup, find_packages

setup(
    name="docker-compose-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=6.0.1",
        "pytest>=7.4.0",
        "python-dotenv>=1.0.0",
        "Jinja2>=3.1.2",
    ],
    python_requires=">=3.8",
) 