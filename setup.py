# import multiprocessing to avoid this bug
# (http://bugs.python.org/issue15881#msg170215)
import multiprocessing
assert multiprocessing
import re
import os
from setuptools import setup, find_packages

module_name = "scanpointgenerator"


def get_version():
    """Extracts the version number from the version.py file.
    """
    VERSION_FILE = os.path.join(module_name, 'version.py')
    txt = open(VERSION_FILE).read()
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', txt, re.M)
    if mo:
        version = mo.group(1)
        bs_version = os.environ.get('MODULEVER', '0.0')
        assert bs_version == "0.0" or bs_version == version, \
            "Version {} specified by the build system doesn't match {} in " \
            "version.py".format(bs_version, version)
        return version
    else:
        raise RuntimeError('Unable to find version string in {0}.'
                           .format(VERSION_FILE))

setup(
    name=module_name,
    version=get_version(),
    description='Python generators for malcolm and GDA scans',
    long_description=open("README.rst").read(),
    url='https://github.com/dls_controls/scanpointgenerator',
    author='Tom Cobb',
    author_email='tom.cobb@diamond.ac.uk',
    keywords='',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
    license='APACHE',
    install_requires=[],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=[
        'nose>=1.3.0',
    ],
    zip_safe=False,
)
