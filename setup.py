import logging
from setuptools import find_packages, setup

# Configure logging to stdout with INFO level
logging.basicConfig(level=logging.INFO)

setup(
    name='text_sumarization',
    version='0.0.0',
    author="Abhishek gupta",
    author_email='abhishek18895gupta@gmail.com',
    packages=find_packages()
)
