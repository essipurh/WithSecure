from setuptools import setup, find_packages  # type: ignore

setup(
    name="batching-library",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
