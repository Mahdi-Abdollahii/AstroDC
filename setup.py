import os
import sys
import shutil
from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='AstroDC',
    version='1.0.5',    
    description='A simple Python package helps us to clean and prepare data related to astronomy and astrophysics',
    url='https://github.com/Mahdi-Abdollahii/AstroDC',
    author='Mahdi',
    author_email='mahdiabdollahii96@gmail.com',
    license='MIT',
    packages=['AstroDC'],
    install_requires=required,
    package_data={},
    include_package_data=False,
)
