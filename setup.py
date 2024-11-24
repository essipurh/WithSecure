from setuptools import setup, find_packages # type: ignore


# Read the requirements from requirements.txt
def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="batching-library",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=read_requirements(),  # Read requirements.txt for dependencies
    python_requires=">=3.12",  # Specify the minimum Python version
)
