import os
import sys
import shutil
from distutils.core import setup
from setuptools import find_packages

print(sys.argv)

if sys.argv[1] != "install":
    shutil.copy('../protocol.json', 'p2_app_protocol/data/protocol.json')

setup(name='p2_app_protocol',
      version='1.0.5',
      author='Johannes Schrimpf',
      author_email='johannes.schrimpf@blueye.no',
      url='https://github.com/BluEye-Robotics/p2_app_protocol',
      package_dir= {'p2_app_protocol': 'p2_app_protocol'},
      package_data= {'p2_app_protocol': ['data/protocol.json']},
      packages=find_packages('.'),
)