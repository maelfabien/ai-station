import os
from setuptools import setup


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name='ai-station',
    version='0.0.1',
    description='A swiss knife for building your next machine learning project.',
    url='https://github.com/fmikaelian/ai-station',
    author='',
    license='MIT',
    packages=['station'],
    install_requires=read('requirements.txt').split(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ais=station:main'
        ]
    }
)
