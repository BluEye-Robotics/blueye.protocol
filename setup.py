# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['blueye', 'blueye.protocol']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17,<2.0']

setup_kwargs = {
    'name': 'blueye.protocol',
    'version': '1.1.2',
    'description': 'Python protocol definition for the Blueye Pioneer',
    'long_description': None,
    'author': 'Sindre Hansen',
    'author_email': 'sindre.hansen@blueye.no',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
