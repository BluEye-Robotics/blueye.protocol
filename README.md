# blueye.protocol
[![Tests](https://github.com/BluEye-Robotics/blueye.protocol/workflows/Tests/badge.svg)](https://github.com/BluEye-Robotics/blueye.protocol/actions)


## About
This repository contains a python library that defines how to communicate with the underwater drones made by [Blueye Robotics](https://blueyerobotics.com).

The protocol itself is defined in another repository, [ProtocolDefinitions](https://github.com/BluEye-Robotics/ProtocolDefinitions), as is stored as a submodule in this repository. The python code in this repository is (mostly) generated from those definitions.

The `blueye.protocol` package's primary use case is in the [`blueye.sdk`](https://github.com/BluEye-Robotics/blueye.sdk). The SDK implements the necessary "plumbing" to utilize the protocol defined here in `blueye.protocol`, and will make interacting with the Blueye drones much easier. If you wish to interact with the drones in your own project we recommend using the `blueye.sdk` package, not `blueye.protocol` directly.

This package requires Python 3.10 or newer.

## Installation
```shell
pip install blueye.protocol
```

## Development

### Dependency/Package management
We use `uv` for dependency/package management, see the [uv docs](https://docs.astral.sh/uv/getting-started/installation/) for installation instructions.


### Code generators
**Important**: This repository includes generated code. If the protocol definitions are changed the generated files need to be updated and committed. The generators are run with:

`invoke generate-udp`

`invoke generate-tcp`

`invoke generate-proto`


### Tests
The tests are located in the `tests` folder, and written using the `pytest` library.

The tests can be run using invoke (to ensure that the protocol files are updated)

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

If you are running MacOS, you need to install gnu-tar
``` shell
brew install gnu-tar
```

and then run the follwing line before the invoke command:
``` shell
PATH="/opt/homebrew/opt/gnu-tar/libexec/gnubin:$PATH"
```

**Be sure to run this script and commit the `setup.py` file when the dependencies have
changed.**
