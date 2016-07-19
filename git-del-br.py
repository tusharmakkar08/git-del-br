import argparse
import logging
import os
import time

__author__ = 'tusharmakkar08'

logger = logging.getLogger('git-del-br')
FORMAT = "%(asctime)-15s:@%(lineno)s %(message)s"
formatter = logging.Formatter(FORMAT)
file_handler = logging.FileHandler("git-del-br.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def delete_remote_merged_branches(branches):
    logger.debug("Deleting remote branches %s", branches)
    for branch in branches:
        cmd = 'git push origin --delete ' + ''.join(branch.split('origin/')[1:])
        answer = os.popen(cmd).read()
        logger.debug("%s", answer)
    pass


def delete_local_merged_branches(branches):
    logger.debug("Deleting local branches %s", branches)
    for branch in branches:
        cmd = 'git branch -D ' + branch
        answer = os.popen(cmd).read()
        logger.debug("%s", answer)


def get_merged_branches(branch_name, remote_flag=False):
    logger.debug("Getting Merged Branches %s %s", branch_name, remote_flag)
    remote_var = ''
    if remote_flag:
        remote_var = '-r'
    cmd = 'git branch ' + remote_var + ' --merged ' + branch_name + """ | grep -v "\*" | grep -v master"""
    answer = os.popen(cmd).read()
    return [i.strip() for i in answer.split('\n') if i]


def filter_time(branches, time_to_remove):
    logger.debug("Filtering on basis of time %s time %s", branches, time_to_remove)
    if time_to_remove == -1:
        return branches
    filtered_branches = []
    for branch in branches:
        cmd = 'echo `git show --format="%ct" ' + branch + '| head -n 1`;'
        answer = os.popen(cmd).read()
        if (int(time.time()) - int(answer)) / 86400 > time_to_remove:
            filtered_branches.append(branches)
    return filtered_branches


def filter_suffix(branches, suffix):
    logger.debug("Filtering on basis of suffix %s suffix %s", branches, suffix)
    return [branch for branch in branches if branch.endswith(suffix)]


def filter_prefix(branches, prefix):
    logger.debug("Filtering on basis of prefix %s prefix %s", branches, prefix)
    return [branch for branch in branches if branch.startswith(prefix)]


def view_and_delete_branches(list_flag, branch_name, prefix, suffix, remote_flag, local_flag, time_to_remove):
    if remote_flag:
        branches_to_remove = filter_time(
            filter_suffix(filter_prefix(get_merged_branches(branch_name, remote_flag), prefix), suffix),
            time_to_remove)
        logger.debug("Viewing remote %s delete flag %s", branches_to_remove, not list_flag)
        if not list_flag:
            delete_remote_merged_branches(branches_to_remove)
    if local_flag:
        branches_to_remove = filter_time(
            filter_suffix(filter_prefix(get_merged_branches(branch_name), prefix), suffix), time_to_remove)
        logger.debug("Viewing local branches %s delete flag %s", branches_to_remove, not list_flag)
        if not list_flag:
            delete_local_merged_branches(branches_to_remove)


def _get_parser():
    """
    Command line Parser for search
    :return:
    """
    parser = argparse.ArgumentParser(description='Tool for deleting remote and local merged branches from Git')
    parser.add_argument('-ls', '--list', action='store_true',
                        help='Lists the branches (not delete)')
    parser.add_argument('-r', '--remote', action='store_true',
                        help='remove merged branches')
    parser.add_argument('-l', '--local', action='store_true',
                        help='Remove local branches')
    parser.add_argument('-a', '--all', action='store_true',
                        help='Removes both local and remote merged branches')
    parser.add_argument('-t', '--time', metavar='time', type=int, default=-1,
                        help='All branches after t-time which the branch is merged (in days) '
                             'default = -1 means infinite days')
    parser.add_argument('-br', '--branch', metavar='branch', type=str, default='master',
                        help='Branch from which other branches will be analysed (default = master)')
    parser.add_argument('-pre', '--prefix', metavar='prefix', type=str, default='',
                        help='Filter branches based on prefix')
    parser.add_argument('-suf', '--suffix', metavar='suffix', type=str, default='',
                        help='Filter branches based on suffix')
    return parser


def command_line_runner():
    """
    Entry point for script; Modify to add another search script
    :return:
    """
    parser = _get_parser()
    args = vars(parser.parse_args())
    if args['all']:
        args['remote'] = True
        args['local'] = True
    if any([args['remote'], args['local']]):
        view_and_delete_branches(args['list'], args['branch'], args['prefix'], args['suffix'],
                                 args['remote'], args['local'], args['time'])
    else:
        parser.print_help()
    return


if __name__ == '__main__':
    command_line_runner()
    logger.debug("\n=============\n")
