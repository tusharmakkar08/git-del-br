import argparse
import os

__author__ = 'tusharmakkar08'


def delete_remote_merged_branches(branches):
    print "deleting remote", branches
    pass


def delete_local_merged_branches(branches):
    print "deleting local", branches
    pass


def get_remote_merged_branches(branch_name, remote_flag):
    print "getting remote merged branches", branch_name
    remote_var = ''
    if remote_flag:
        remote_var = '-r'
    cmd = 'git branch ' + remote_var + ' --merged ' + branch_name + \
          """ | grep -v "\*" | grep -v master | xargs -L1 | awk '{split($0,a,"/"); print a[2]}'"""
    answer = os.popen(cmd).read()
    return [i.strip() for i in answer.split('\n') if i]


def filter_time(branches, time_to_remove):
    print "filtering on basis of time", branches, time_to_remove
    return []


def filter_suffix(branches, suffix):
    print "filtering on basis of suffix", branches, suffix
    return [branch for branch in branches if branch.endswith(suffix)]


def filter_prefix(branches, prefix):
    print "filtering on basis of prefix", prefix, branches
    return [branch for branch in branches if branch.startswith(prefix)]


def view_and_delete_branches(list_flag, branch_name, prefix, suffix, remote_flag, local_flag, time_to_remove):
    if remote_flag:
        branches_to_remove = filter_time(
            filter_suffix(filter_prefix(get_remote_merged_branches(branch_name, remote_flag), prefix), suffix),
            time_to_remove)
        print "viewing remote", branches_to_remove
        if not list_flag:
            delete_remote_merged_branches(branches_to_remove)
    if local_flag:
        branches_to_remove = filter_time(
            filter_suffix(filter_prefix(get_remote_merged_branches(branch_name), prefix), suffix), time_to_remove)
        print "viewing local", branches_to_remove
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
                        help='Lists all branches after t-time which the branch is merged and not changed (in days) '
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
