git-del-br
==========

|GitHub issues| |GitHub stars| |GitHub license| |PyPI|

Deleting Merged Branches

Usage:
======

::

            usage: git-del-br [-h] [-ls] [-r] [-l] [-a] [-t time] [-br branch]
                                 [-pre prefix] [-suf suffix]
            
            Tool for deleting remote and local merged branches from Git
            
            optional arguments:
              -h, --help            show this help message and exit
              -ls, --list           Lists the branches (not delete)
              -r, --remote          remove merged branches
              -l, --local           Remove local branches
              -a, --all             Removes both local and remote merged branches
              -t time, --time time  All branches after t-time which the branch is merged
                                    (in days) default = -1 means infinite days
              -br branch, --branch branch
                                    Branch from which other branches will be analysed
                                    (default = current_branch)
              -pre prefix, --prefix prefix
                                    Filter branches based on prefix
              -suf suffix, --suffix suffix
                                    Filter branches based on suffix

You can find more details about the project `here`_.

Examples:
=========

-  For listing remote merged branches which haven’t been touched since
   past 3 months (last commit was 3 months ago)

   ::

           git-del-br -ls -r -t=90

For deleting those branches

::

            git-del-br -r -t=90

-  For listing local branches which start with ``dev`` prefix

   ::

           git-del-br -ls -l -pre='dev'

For deleting those branches

::

            git-del-br -l -pre='dev'

INSTALL:
========

You can install this from pip using ``pip install git-del-br``.

CONTRIBUTION:
=============

Fork the project. Create a branch from ``master`` or ``gh-pages`` and
submit a PR to the same.

LICENSE:
========

The mighty MIT license. Please check ``LICENSE`` for more details.

.. _here: http://tusharmakkar08.github.io/git-del-br

.. |GitHub issues| image:: https://img.shields.io/github/issues/tusharmakkar08/git-del-br.svg
   :target: https://github.com/tusharmakkar08/git-del-br/issues
.. |GitHub stars| image:: https://img.shields.io/github/stars/tusharmakkar08/git-del-br.svg
   :target: https://github.com/tusharmakkar08/git-del-br/stargazers
.. |GitHub license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/tusharmakkar08/git-del-br/master/LICENSE
.. |PyPI| image:: https://img.shields.io/pypi/v/git-del-br.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/git-del-br
