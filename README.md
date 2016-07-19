# git-del-br
Deleting Merged Branches 

Usage:
======

            usage: git_del_br [-h] [-ls] [-r] [-l] [-a] [-t time] [-br branch]
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
                                    (default = master)
              -pre prefix, --prefix prefix
                                    Filter branches based on prefix
              -suf suffix, --suffix suffix
                                    Filter branches based on suffix


INSTALL:
========

You can install this from pip using `pip install git-del-br`.

LICENSE:
========

The mighty MIT license. Please check `LICENSE` for more details.
