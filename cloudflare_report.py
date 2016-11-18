from __future__ import absolute_import
from __future__ import print_function


import cloudflare_cli
import cloudflare_filter_records
import cloudflare_yaml_io


def main():
    cli_arg_params = cloudflare_cli.cli_args()

    zone_record_dict = cloudflare_yaml_io.read_yaml_backup_file()

    filter_list_dict = cloudflare_filter_records.filter_stack(
        zone_record_dict, cli_arg_params['domain'], cli_arg_params['stack'])
    print(filter_list_dict)

    print('Finished processing all records!!!')


if __name__ == '__main__':
    main()
