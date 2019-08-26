# blueye.protocol
[![Test status](https://github.com/BluEye-Robotics/p2_app_protocol/workflows/PythonTests/badge.svg)](https://github.com/BluEye-Robotics/p2_app_protocol/actions)

This repository provides the definition of the UDP and TCP drone-app protocol in the form of a two json files (udp_protocol.json, and tcp_protocol.json). Python code is generated based on the protocol definition for receiving UDP messages with telemetry from the drone and sending commands to the drone over TCP using the TCP client.
Poetry is used for dependency management and packaging.

## Setup python version and packages for development
Install poetry, for more instructions see the [poetry repo](https://github.com/sdispater/poetry)

``` shell
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Install pyenv, for more instructions see the [pyenv-installer](https://github.com/pyenv/pyenv-installer)

``` shell
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
pyenv update
```

Install the needed dependencies for building python 3.7.4 , then build python in pyenv
``` shell
apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl
pyenv install 3.7.4
```

Create a virtual environment, and activate it
``` shell
pyenv virtualenv 3.7.4 blueye_protocol
pyenv activate blueye_protocol
```

Install the python packages needed by the battery tester using poetry in the projects root directory

``` shell
poetry install
```

## Code generators
Important: This repository includes generated code. If `udp_protocol.json` or `tcp_protocol.json` are changed, the two generated filed in `/blueye/protocol/` `tcp_protocol_class.py` and `udp_protocol_dict.py` need to be updated and later committed.

The generated protocol files are updated using the generators in the `generators` folder. The generator are run when running the tests.
```
invoke test
```

## Tests
Test for the TCP client are written using pytest. Test for UDP client are written using unittest. All tests are run using pytest. The tests can be run using invoke.

``` shell
invoke test
```
Or directly using pytest.

``` shell
pytest
```

All changes need to be backwards-compatible.

**Important:
Make sure to update meta-blueye but also the the Yocto SDK after protocol changes, otherwise cross compilation might fail and will not be compatible.**
