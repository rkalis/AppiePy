# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='appiepy',
    version='0.1.0',
    description='A Python API for Albert Heijn',
    long_description=long_description,
    url='https://github.com/rkalis/AppiePy',
    author='Rosco Kalis',
    author_email='roscokalis@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='albert heijn API nutrition price',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    python_requires='~=3.4',
    extras_require={
        # 'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    package_data={
        # 'sample': ['package_data.dat'],
    },
    # data_files=[('my_data', ['data/data_file'])],
    entry_points={
        # 'console_scripts': [
        #     'sample=sample:main',
        # ],
    },
    project_urls={
        'GitHub': 'https://github.com/rkalis/AppiePy',
        'Issues': 'https://github.com/rkalis/AppiePy/issues'
    },
)
