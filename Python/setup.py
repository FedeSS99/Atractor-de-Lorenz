from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext = Extension("CalculoAtractorLorenz", ["CalculoAtractorLorenz.pyx"],
                include_dirs = [numpy.get_include()])

setup(ext_modules=[ext], cmdclass={"build_ext": build_ext})
