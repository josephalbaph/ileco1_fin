# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ileco1_fin/__init__.py
from ileco1_fin import __version__ as version

setup(
	name='ileco1_fin',
	version=version,
	description='ILECO-1 Finance',
	author='Joseph Marie M. Alba',
	author_email='josephalbaph@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
