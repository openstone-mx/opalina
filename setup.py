import os
import json
from typing import Dict
from setuptools import setup, find_namespace_packages


CODEBASE_PATH = os.environ.get(
    "CODEBASE_PATH",
    default=os.path.join("src", "main"),
)

with open("requirements.txt", "r") as file:
    requirements = [
        line
        for line in file.read().splitlines()
        if line and not line.startswith("#")
    ]

with open((version_filepath := os.path.join(CODEBASE_PATH, "opalina", "version")), "r") as file:
    version = file.read().strip()

with open("README.md") as file:
    readme = file.read()

setup(
    name="opalina",
    version=version,
    description="Opalina Featherweight Data Lineage for Apache Spark",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://opalina.openstone.mx",
    author="Rodrigo H. Mota",
    author_email="code@rhdzmota.com",
    packages=find_namespace_packages(where=CODEBASE_PATH),
    package_dir={
        "": CODEBASE_PATH
    },
    package_data={
        "": [
            version_filepath,
        ]
    },
    entry_points={
        "console_scripts": [
            "opalina=opalina.cli:CLI.cli_exec",
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.11.0"
)
