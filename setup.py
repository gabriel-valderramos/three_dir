from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    req = f.readlines()

setup(
    name='three_dir',
    version='1.0',
    packages=["three_dir"],
    url='',
    license='MIT',
    author='Gabriel Valderramos',
    author_email='gabrielvalderramos@gmail.com',
    description='List all files recursively and save them into json or yaml file',
    install_requires=req,
)
