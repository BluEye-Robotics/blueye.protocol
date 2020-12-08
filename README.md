# blueye.protocol
[![Tests](https://github.com/BluEye-Robotics/blueye.protocol/workflows/PythonTests/badge.svg)](https://github.com/BluEye-Robotics/blueye.protocol/actions)

This repository contains a python library that defines how to communicate with the
Blueye Pioneer. The Blueye Pioneer is an underwater drone made by Blueye Robotics, see
[blueyerobotics.com](https://blueyerobotics.com) for more information.

The protocol itself is defined in two json files, one for UDP and one for TCP. These are
stored as a submodule in this repository, and the python code is generated from these
definitions.

This package requires Python 3.7 or newer.

The `blueye.protocol` package's main use is in the
[`blueye.sdk`](https://github.com/BluEye-Robotics/blueye.sdk). The SDK implements a
layer of convenience on top of the TCP and UDP clients found here in `blueye.protocol`,
to make interacting with the Pioneer easier. If you want to interact with the Pioneer in
your own project we recommend using the
[`blueye.sdk`](https://github.com/BluEye-Robotics/blueye.sdk) package, not
`blueye.protocol` directly.

## Installation
```shell
pip install blueye.protocol
```

## Development

### Install poetry
We use Poetry for package management, install it like this

``` shell
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

for more instructions see the [Poetry repository](https://github.com/sdispater/poetry).

### Install the necessary Python version
We require Python v3.7 or newer, and many operating systems package an older version of
Python the easiest (for Linux/OS X) is to use pyenv. Pyenv manages multiple Python
versions in parallel for you.

The instructions below are for Linux (Ubuntu), but pyenv exist both for
[macOS](https://github.com/pyenv/pyenv#homebrew-on-macos) and
[Windows](https://github.com/pyenv-win/pyenv-win) and the instructions should be fairly
similar.

Install pyenv, for more instructions see the [pyenv-installer](https://github.com/pyenv/pyenv-installer)

``` shell
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
pyenv update
```

Install the needed dependencies for building python 3.7.4
``` shell
apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```
Then build python with pyenv
``` shell
pyenv install 3.7.4
```

### Create a virtual environment and install the dependencies
Using a virtual environment is not strictly necessary, but it greatly simplifies the
development of Python packages.

Since we already have pyenv installed we'll use it to create a virtual environment,

``` shell
pyenv virtualenv 3.7.4 blueye_protocol
pyenv activate blueye_protocol
```

Now we're ready to install the python packages needed, by running poetry in the
projects root directory

``` shell
poetry install
```

### Code generators
**Important**: This repository includes generated code. If the protocol definitions are
changed the generated files need to be updated and committed.
The generated protocol files are updated using the generators in the `generators`
folder. They can be run with `invoke generate-udp` or `invoke generate-tcp`.
The generators are run automatically before testing with.

``` shell
invoke test
```

### Tests
Test for the TCP client are written using pytest. Test for UDP client are written using
unittest. All tests are run using pytest. The tests can be run using invoke (to ensure
that the protocol files are updated)

``` shell
invoke test
```
or directly using pytest (if you don't want to generate the definitions)

``` shell
pytest
```

### `setup.py`
Since bitbake doesn't have support for pyproject.toml files yet, we need to include a
`setup.py` file to specify the dependencies needed. There's an invoke task for
generating the file that can be run with
``` shell
invoke generate-setup-py
```

**Be sure to run this script and commit the `setup.py` file when the dependencies have
changed.**
