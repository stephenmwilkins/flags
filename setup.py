#!/usr/bin/env python

from distutils.core import setup

setup(name='flags',
      version='0.1',
      description='First Light and Assembly of Galaxies python',
      author='Stephen Wilkins',
      install_requires=[  
        "h5py",
        "astropy",
        "numpy",
        "scipy",
        "unyt",
        "matplotlib",
        "cmasher",
      ],
      packages=['flags', 'flags.pz', 'flags.surveys'],
)