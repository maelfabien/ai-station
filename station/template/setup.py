import os
from setuptools import setup


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name='{{ project_name }}',
    version='0.0.1',
    description='',
    url='https://github.com/{{ project_author }}/{{ project_name }}',
    author='{{ project_author }}',
    license='MIT',
    packages=['{{ project_name }}'],
    install_requires=read('requirements/requirements-python.txt').split()
)
