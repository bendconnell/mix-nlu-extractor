from setuptools import setup, find_packages

setup(
    name="nlu-extractor",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.8",
    author="",
    description="NLU Extractor project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)