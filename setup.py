from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='project_lambda_exchange',
    version='1.0.2',
    description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dispiny/python-hello-packages",
    author='Jongmin Park',
    author_email='jongmin.park@samsung.com',
    packages=find_packages(),  
    python_requires='>=3.6'
)