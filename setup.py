__author__ = 'tusharmakkar08'

from pip.req import parse_requirements
from setuptools import setup

# install_reqs = parse_requirements('requirements.txt', session=False)
# install_requirement = [str(ir.req) for ir in install_reqs]

setup(
    # Application name:
    name="git-del-br",

    # Version number:
    version="0.0.1",

    # Application author details:
    author="Tushar Makkar",
    author_email="tusharmakkar08@gmail.com",

    # Packages
    py_modules=['fb_search'],

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

    long_description=open("README.md").read(),

    entry_points={
        'console_scripts': [
            'git-del-br = git-del-br:command_line_runner',
        ]
    },

    # Dependent packages (distributions)
    # install_requires=install_requirement,

)
