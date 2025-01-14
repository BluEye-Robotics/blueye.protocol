# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blueye', 'blueye.protocol', 'blueye.protocol.types', 'blueye.protocol.v2']

package_data = \
{'': ['*']}

install_requires = \
['proto-plus>=1.22.1,<2.0.0', 'setuptools>=40']

extras_require = \
{':python_version >= "3.9" and python_version < "3.13"': ['numpy>=1.26,<2.0']}

setup_kwargs = {
    'name': 'blueye.protocol',
    'version': '2.7.0',
    'description': 'Python protocol definition for the Blueye drones',
    'long_description': '# blueye.protocol\n[![Tests](https://github.com/BluEye-Robotics/blueye.protocol/workflows/Tests/badge.svg)](https://github.com/BluEye-Robotics/blueye.protocol/actions)\n\n**Deprecation notice**\n\nBlunux 3.0 introduces a new protocol based on [Protobuf](https://developers.google.com/protocol-buffers/) messages passed over a [ZeroMQ](https://zeromq.org/) layer. Starting with Blunux 3.1 the old TCP/UDP based protocol will no longer be supported/compatible.\n\n\n## About\nThis repository contains a python library that defines how to communicate with the underwater drones made by [Blueye Robotics](https://blueyerobotics.com).\n\nThe protocol itself is defined in another repository, [ProtocolDefinitions](https://github.com/BluEye-Robotics/ProtocolDefinitions), as is stored as a submodule in this repository. The python code in this repository is (mostly) generated from those definitions.\n\nThe `blueye.protocol` package\'s primary use case is in the [`blueye.sdk`](https://github.com/BluEye-Robotics/blueye.sdk). The SDK implements the necessary "plumbing" to utilize the protocol defined here in `blueye.protocol`, and will make interacting with the Blueye drones much easier. If you wish to interact with the drones in your own project we recommend using the `blueye.sdk` package, not `blueye.protocol` directly.\n\nThis package requires Python 3.8 or newer.\n\n## Installation\n```shell\npip install blueye.protocol\n```\n\n## Development\n\n### Dependency/Package management\nWe use Poetry for dependency/package management, see the [Poetry docs](https://python-poetry.org/docs/) for installation instructions.\n\n\n### Code generators\n**Important**: This repository includes generated code. If the protocol definitions are changed the generated files need to be updated and committed. The generators are run with:\n\n`invoke generate-udp`\n\n`invoke generate-tcp`\n\n`invoke generate-proto`\n\n\n### Tests\nThe tests are located in the `tests` folder, and written using the `pytest` library.\n\nThe tests can be run using invoke (to ensure that the protocol files are updated)\n\n``` shell\ninvoke test\n```\nor directly using pytest (if you don\'t want to generate the definitions)\n\n``` shell\npytest\n```\n\n### `setup.py`\nSince bitbake doesn\'t have support for pyproject.toml files yet, we need to include a\n`setup.py` file to specify the dependencies needed. There\'s an invoke task for\ngenerating the file that can be run with\n``` shell\ninvoke generate-setup-py\n```\n\nIf you are running MacOS, you need to install gnu-tar\n``` shell\nbrew install gnu-tar\n```\n\nand then run the follwing line before the invoke command:\n``` shell\nPATH="/opt/homebrew/opt/gnu-tar/libexec/gnubin:$PATH"\n```\n\n**Be sure to run this script and commit the `setup.py` file when the dependencies have\nchanged.**\n',
    'author': 'Sindre Hansen',
    'author_email': 'sindre.hansen@blueye.no',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.blueyerobotics.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
