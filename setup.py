# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['blueye', 'blueye.protocol']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17,<2.0', 'setuptools>=40']

setup_kwargs = {
    'name': 'blueye.protocol',
    'version': '1.1.2',
    'description': 'Python protocol definition for the Blueye Pioneer',
    'long_description': "# blueye.protocol\n[![Tests](https://github.com/BluEye-Robotics/blueye.protocol/workflows/PythonTests/badge.svg)](https://github.com/BluEye-Robotics/blueye.protocol/actions)\n\nThis repository provides the definition of the UDP and TCP drone <--> app protocol in the form of two json files (`udp_protocol.json`, and `tcp_protocol.json`). Python code is generated based on the protocol definitions for receiving UDP messages with telemetry from the drone and sending commands to the drone over TCP.\nPoetry is used for dependency management and packaging.\n\n## Installation\n```shell\npip install blueye.protocol\n```\n\n## Development\n\n### Setup python version and packages for development\nInstall poetry, for more instructions see the [poetry repo](https://github.com/sdispater/poetry)\n\n``` shell\ncurl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python\n```\n\nInstall pyenv, for more instructions see the [pyenv-installer](https://github.com/pyenv/pyenv-installer)\n\n``` shell\ncurl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash\npyenv update\n```\n\nInstall the needed dependencies for building python 3.7.4\n``` shell\napt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \\\nlibreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \\\nxz-utils tk-dev libffi-dev liblzma-dev python-openssl\n```\nThen build python with pyenv\n``` shell\npyenv install 3.7.4\n```\n\nCreate a virtual environment, and activate it\n``` shell\npyenv virtualenv 3.7.4 blueye_protocol\npyenv activate blueye_protocol\n```\n\nInstall the python packages needed by the using poetry in the projects root directory\n\n``` shell\npoetry install\n```\n\n### Code generators\nImportant: This repository includes generated code. If `udp_protocol.json` or `tcp_protocol.json` are changed, the two generated filed in `/blueye/protocol/` `tcp_protocol_class.py` and `udp_protocol_dict.py` need to be updated and later committed.\n\nThe generated protocol files are updated using the generators in the `generators` folder. They can be run with `invoke generate_udp` or `invoke generate_tcp`. The generators are run automatically before testing with.\n\n``` shell\ninvoke test\n```\n\n### Tests\nTest for the TCP client are written using pytest. Test for UDP client are written using unittest. All tests are run using pytest. The tests can be run using invoke.\n\n``` shell\ninvoke test\n```\nOr directly using pytest.\n\n``` shell\npytest\n```\n\n### `setup.py`\nSince bitbake doesn't have support for pyproject.toml files yet, we need to include a\n`setup.py` file to specify the dependencies needed. There's an invoke task for\ngenerating the file that can be run with\n``` shell\ninvoke generate-setup-py\n```\n\n**Be sure to run this script and commit the `setup.py` file when the dependencies have\nchanged.**\n",
    'author': 'Sindre Hansen',
    'author_email': 'sindre.hansen@blueye.no',
    'url': 'https://www.blueyerobotics.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
