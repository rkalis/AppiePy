from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    readme = f.read()

setup(
    name='appiepy',
    version='0.2.4',
    description='A Python API for Albert Heijn',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/rkalis/AppiePy',
    author='Rosco Kalis',
    author_email='roscokalis@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='albert heijn products API nutrition price',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    python_requires='~=3.4',
    extras_require={
        'dev': ['twine'],
        'test': ['nose', 'coverage'],
    },
    setup_requires=['wheel'],
    project_urls={
        'GitHub': 'https://github.com/rkalis/AppiePy',
        'Issues': 'https://github.com/rkalis/AppiePy/issues'
    },
)
