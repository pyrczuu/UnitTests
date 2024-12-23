import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="attendance",
    version=version,
    author="Damian Pyrcz",
    author_email="damian.pyrcz@edu.uekat.pl",
    description="Very basic attendance system for SON",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pyrczuu/UnitTests",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["UnitTests=src.cli.cli:main"],
    },
    python_requires=">=3.12",
)
