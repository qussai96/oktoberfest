# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oktoberfest']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.0,<2.0.0', 'pandas>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'oktoberfest',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

# This setup.py was autogenerated using poetry.
