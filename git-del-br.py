import argparse

__author__ = 'tusharmakkar08'


def delete_remote_merged_branches():
    print "remote"
    pass


def delete_local_merged_branches():
    print "local"
    pass


def _get_parser():
    """
    Command line Parser for search
    :return:
    """
    parser = argparse.ArgumentParser(description='Tool for deleting remote and local merged branches from Git')
    parser.add_argument('-r', '--remote', action='store_true',
                        help='remove merged branches')
    parser.add_argument('-l', '--local', action='store_true',
                        help='Remove local branches')
    parser.add_argument('-a', '--all', action='store_true',
                        help='Removes both local and remote merged branches')
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
        if args['remote']:
            delete_remote_merged_branches()
        if args['local']:
            delete_local_merged_branches()
    else:
        parser.print_help()
    return


if __name__ == '__main__':
    command_line_runner()
