from setuptools import setup, find_packages
from setuptools.command.install import install
import os


setup(
    name='slackaps',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Francesco De Carlo, Tao Zhou, Fanny Rodolakis, Byeongdu Lee',
    author_email='decarlof@gmail.com',
    url='https://github.com/xray-imaging/slackaps',
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/slackaps'],
    description='cli to run a slack rob at the APS',
    zip_safe=False,
)