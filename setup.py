__author__ = 'junaid'

from setuptools import setup, find_packages
setup(
    # basic package data
    name = "OneBackup",
    version = "0.1",
    # package structure
    packages=find_packages('src'),
    package_dir={'':'src'},

    # install executable
    entry_points = {
        'console_scripts' : [
            'onebackup = onebackup.app:main'
        ]

    },

    install_requires = [

    ],

)
