from setuptools import setup, find_packages
from materpyom import __version__

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="materpyom",
    version=__version__,
    description="Read and write functiosn to materiom database",
    author="Peter Dudfield",
    author_email="peter.dudfield@hotmail.com",
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
)
