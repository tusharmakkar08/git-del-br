__author__ = 'tusharmakkar08'

from setuptools import setup

setup(
    # Application name:
    name="git-del-br",

    # Version number:
    version="1.0.5",

    # Application author details:
    author="Tushar Makkar",
    author_email="tusharmakkar08@gmail.com",

    # Packages
    py_modules=['git_del_br'],

    package_data={'': ['*.md']},

    license='MIT',
    platforms=['any'],
    # Details
    url="https://github.com/tusharmakkar08/git-del-br/",

    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],

    # license="LICENSE.txt",
    description="Git delete merged branches",

    long_description=open("README.rst").read(),

    entry_points={
        'console_scripts': [
            'git-del-br=git_del_br:command_line_runner',
        ]
    },

)
