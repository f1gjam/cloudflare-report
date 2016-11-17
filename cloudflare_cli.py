from __future__ import absolute_import
from __future__ import print_function

import argparse


def cli_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '--disable',
        action='store_true',
        default=None,
        help='Sets Cloudflare Proxy to OFF/Disable')
    group.add_argument(
        '--restore',
        action='store_false',
        default=None,
        help='Restores Cloudflare proxy settings to those in the backup file')
    parser.add_argument(
        '--domain', default=None, help='domain for stack', required=True)
    parser.add_argument(
        '--stack',
        default=None,
        help='stack to disable/restore',
        required=True)
    parser.parse_args()
    args = parser.parse_args()

    print(args)
    if args.disable or args.restore is not None and args.domain and args.stack is not None:
        if args.disable is True:
            print('Disabing Proxy')

            cli_arg_params = {
                "flag": True,
                "domain": args.domain,
                "stack": args.stack
            }
            return cli_arg_params

        elif args.restore is False:
            print('Restoring Proxy settings')

            cli_arg_params = {
                "flag": False,
                "domain": args.domain,
                "stack": args.stack
            }
            return cli_arg_params

    else:
        print(parser.print_help())
