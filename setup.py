from distutils.core import setup
import py2exe, os, sys

setup(console=["main.py"], requires=['psutil'])
