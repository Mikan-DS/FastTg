from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='FastTg',
    version='1.23',
    packages=find_packages(),
    install_requires=required,
)