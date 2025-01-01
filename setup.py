from setuptools import find_packages, setup

setup(
    name="src",  # Name of the package
    version="0.1",
    author="Arjun",
    author_email="your.email@example.com",
    description="Your project description",
    packages=find_packages(),  # Automatically find and include all packages under `src/`
    # install_requires=[],  # Add any dependencies here
)
