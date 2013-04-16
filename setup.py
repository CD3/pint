#!/usr/bin/env python
"""
Pint: a Python units library
============================

Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. Due to it's modular design, you to extend (or even rewrite!)
the complete list without changing the source code.

It has a complete test coverage. It runs in Python 2.7 and 3.X
with no other dependency. It licensed under BSD.


Design principles
-----------------

Although there are already a few very good Python packages to handle physical
quantities, no one was really fitting my needs. Like most developers, I programed
Pint to scratch my own itches.

- Unit parsing: prefixed and pluralized forms of units are recognized without
  explicitly defining them. In other words: as the prefix *kilo* and the unit *meter*
  are defined, Pint understands *kilometers*. This results in a much shorter and
  maintainable unit definition list as compared to other packages.

- Standalone unit definitions: units definitions are loaded from simple and
  easy to edit text file. Adding and changing units and their definitions does
  not involve changing the code.

- Advanced string formatting: a quantity can be formatted into string using
  PEP 3101 syntax. Extended conversion flags are given to provide latex and pretty
  formatting.

- Small codebase: small and easy to maintain codebase with a flat hierarchy.
  It is a single stand-alone module that can be installed as a package or added
  side by side to your project.

- Dependency free: it depends only on Python and it's standard library.

- Python 2 and 3: A single codebase that runs unchanged in Python 2.6+ and Python 3.0+.

- Experimental advanced NumPy support: While NumPy is not a requirement for Pint,
  when available ndarray methods and ufuncs can be used in Quantity objects.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Pint',
    version='0.1.3',
    description='Physical quantities module',
    long_description=__doc__,
    keywords='physical quantities unit conversion science',
    author='Hernan E. Grecco',
    author_email='hernan.grecco@gmail.com',
    url='https://github.com/hgrecco/pint',
    test_suite='pint.testsuite.testsuite',
    zip_safe=False,
    packages=['pint'],
    package_data={
        'pint': [
        'default_en.txt']},
    
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ])
