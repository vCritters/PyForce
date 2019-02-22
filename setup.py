import os

from setuptools import find_packages
from setuptools import setup

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

# Required packages will be stored in --> requirements.txt
# Read the requirements.txt file 
requirements = read("requirements.txt").split()


setup(
    name='PyForce',
    version='0.1dev'
    author='Aidan and Ryan Wilson',
    description=('Library to make certain activities simpler.'),
    include_package_data=True,
    long_description=read("README.md"),
    install_requires=requirements,
)
