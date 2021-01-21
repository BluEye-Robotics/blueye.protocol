# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blueye', 'blueye.protocol']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17,<2.0', 'setuptools>=40']

setup_kwargs = {
    'name': 'blueye.protocol',
    'version': '1.3.2',
    'description': 'Python protocol definition for the Blueye Pioneer',
    'long_description': "# blueye.protocol\n[![Tests](https://github.com/BluEye-Robotics/blueye.protocol/workflows/PythonTests/badge.svg)](https://github.com/BluEye-Robotics/blueye.protocol/actions)\n\nThis repository contains a python library that defines how to communicate with the\nBlueye Pioneer. The Blueye Pioneer is an underwater drone made by Blueye Robotics, see\n[blueyerobotics.com](https://blueyerobotics.com) for more information.\n\nThe protocol itself is defined in two json files, one for UDP and one for TCP. These are\nstored as a submodule in this repository, and the python code is generated from these\ndefinitions.\n\nThis package requires Python 3.7 or newer.\n\nThe `blueye.protocol` package's main use is in the\n[`blueye.sdk`](https://github.com/BluEye-Robotics/blueye.sdk). The SDK implements a\nlayer of convenience on top of the TCP and UDP clients found here in `blueye.protocol`,\nto make interacting with the Pioneer easier. If you want to interact with the Pioneer in\nyour own project we recommend using the\n[`blueye.sdk`](https://github.com/BluEye-Robotics/blueye.sdk) package, not\n`blueye.protocol` directly.\n\n## Installation\n```shell\npip install blueye.protocol\n```\n\n## Development\n\n### Install poetry\nWe use Poetry for package management, install it like this\n\n``` shell\ncurl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python\n```\n\nfor more instructions see the [Poetry repository](https://github.com/sdispater/poetry).\n\n### Install the necessary Python version\nWe require Python v3.7 or newer, and many operating systems package an older version of\nPython the easiest (for Linux/OS X) is to use pyenv. Pyenv manages multiple Python\nversions in parallel for you.\n\nThe instructions below are for Linux (Ubuntu), but pyenv exist both for\n[macOS](https://github.com/pyenv/pyenv#homebrew-on-macos) and\n[Windows](https://github.com/pyenv-win/pyenv-win) and the instructions should be fairly\nsimilar.\n\nInstall pyenv, for more instructions see the [pyenv-installer](https://github.com/pyenv/pyenv-installer)\n\n``` shell\ncurl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash\npyenv update\n```\n\nInstall the needed dependencies for building python 3.7.4\n``` shell\napt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \\\nlibreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \\\nxz-utils tk-dev libffi-dev liblzma-dev python-openssl\n```\nThen build python with pyenv\n``` shell\npyenv install 3.7.4\n```\n\n### Create a virtual environment and install the dependencies\nUsing a virtual environment is not strictly necessary, but it greatly simplifies the\ndevelopment of Python packages.\n\nSince we already have pyenv installed we'll use it to create a virtual environment,\n\n``` shell\npyenv virtualenv 3.7.4 blueye_protocol\npyenv activate blueye_protocol\n```\n\nNow we're ready to install the python packages needed, by running poetry in the\nprojects root directory\n\n``` shell\npoetry install\n```\n\n### Code generators\n**Important**: This repository includes generated code. If the protocol definitions are\nchanged the generated files need to be updated and committed.\nThe generated protocol files are updated using the generators in the `generators`\nfolder. They can be run with `invoke generate-udp` or `invoke generate-tcp`.\nThe generators are run automatically before testing with.\n\n``` shell\ninvoke test\n```\n\n### Tests\nTest for the TCP client are written using pytest. Test for UDP client are written using\nunittest. All tests are run using pytest. The tests can be run using invoke (to ensure\nthat the protocol files are updated)\n\n``` shell\ninvoke test\n```\nor directly using pytest (if you don't want to generate the definitions)\n\n``` shell\npytest\n```\n\n### `setup.py`\nSince bitbake doesn't have support for pyproject.toml files yet, we need to include a\n`setup.py` file to specify the dependencies needed. There's an invoke task for\ngenerating the file that can be run with\n``` shell\ninvoke generate-setup-py\n```\n\n**Be sure to run this script and commit the `setup.py` file when the dependencies have\nchanged.**\n",
    'author': 'Sindre Hansen',
    'author_email': 'sindre.hansen@blueye.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.blueyerobotics.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
