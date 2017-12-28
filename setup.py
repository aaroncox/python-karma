#!/usr/bin/env python3

from setuptools import setup

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    codecs.register(lambda name, enc=ascii: {True: enc}.get(name == 'mbcs'))

VERSION = '0.1.0'

setup(
    name='karma',
    version=VERSION,
    description='Python library for karma',
    long_description=open('README.md').read(),
    download_url='https://github.com/xeroc/python-karma/tarball/' + VERSION,
    author='',
    author_email='',
    maintainer='',
    maintainer_email='',
    url='',
    keywords=['karma', 'library', 'api', 'rpc'],
    packages=[
        "karma",
        "karma.cli",
        "karmaapi",
        "karmabase",
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
    ],
    entry_points={
        'console_scripts': [
            'karma = karma.cli.cli:main',
        ],
    },
    install_requires=[
        "graphenelib>=0.5.2",
        "scrypt",
        "appdirs",
        "pycrypto",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
)
