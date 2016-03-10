from distutils.core import setup
import py2exe, os, sys

setup(name="sorting",
      version="1.0.1",
      description="visualize sorting algorithms working",
      long_description="shows how ca. 15 in place sorting algorithms sort a given, changeable list",
      author="Nasskalte Juni",
      license="MIT",
      keywords="sorting algorithms visualization",
      console=["main.py"]
      )
