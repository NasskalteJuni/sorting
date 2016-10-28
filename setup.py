#!python3.4
from distutils.core import setup
import py2exe, os, sys
import psutil, multiprocessing

setup(name="sorting",
      version="1.0.1",
      description="visualize sorting algorithms working",
      long_description="shows how ca. 15 in place sorting algorithms sort a given, changeable list",
      author="Nasskalte Juni",
      license="MIT",
      keywords="sorting algorithms visualization",
      requires=["multiprocessing", "psutil"],
      windows=["main.py"],
      icon_resources=[(1, "./sorting_icon.ico")]
      )
