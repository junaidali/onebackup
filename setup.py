__author__ = 'junaid'

from setuptools import setup, find_packages

setup(
    # basic package data
    name = "OneBackup",
    version = "0.1",
    license = 'MIT',
    keywords = "backup restore",
    classifiers=['Environment :: Console',
                 'Intended Audience :: System Administrators',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: System :: Archiving :: Backup'
                 ],
    # package structure
    packages=find_packages('src'),
    package_dir={'':'src'},

    # install executable
    entry_points = {
        'console_scripts' : [
            'onebackup = onebackup.app:main',
            'onebackup-config = onebackup.app:config',
        ]

    },

    install_requires = ['sqlalchemy'],

    # use nose to run tests
    test_suite='nose.collector',
)
