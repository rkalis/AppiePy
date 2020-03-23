# Contributing to AppiePy

## Set up a local development environment

Set up a virtualenv for AppiePy, activate it and install AppiePy's requirements.

```shell
python3 -m venv /path/to/new/virtualenv
source <venv_path>/bin/activate
pip3 install -r requirements.txt
```

## Run tests

```shell
python3 -m unittest
```

## Publishing a new release

```shell
rm -r build/ dist/
python3 setup.py sdist
python3 setup.py bdist_wheel
twine upload dist/*
```
