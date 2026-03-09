from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize(["gaussian.pyx", "sobel.pyx", "median.pyx"]),
    include_dirs=[np.get_include()]
)