from distutils.core import setup
from setuptools import find_packages
setup(name='p2_app_protocol',
      version='1.0.2',
      author='Johannes Schrimpf',
      author_email='johannes.schrimpf@blueye.no',
      url='https://github.com/BluEye-Robotics/p2_app_protocol',
      package_dir= {'p2_app_protocol': 'p2_app_protocol'},
      package_data={'': ['data/protocol.json']},
      packages=find_packages('.'),
      )
