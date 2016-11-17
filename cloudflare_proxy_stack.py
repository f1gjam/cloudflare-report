from __future__ import absolute_import
from __future__ import print_function

import cloudflare_call
import cloudflare_cli
import cloudflare_filter_records
import cloudflare_proxy_setting
import cloudflare_yaml_io


def main():
    cli_arg_params = cloudflare_cli.cli_args()

    cloudflare_details_params = cloudflare_call.cloudflare_details()

    zone_record_dict = cloudflare_yaml_io.read_yaml_backup_file()

    filter_list_dict = cloudflare_filter_records.filter_stack(
        zone_record_dict, cli_arg_params['domain'], cli_arg_params['stack'])

    #cloudflare_proxy_setting.get_record_info(cloudflare_details_params,
    #                                         filter_list_dict, cli_arg_params)

    print(filter_list_dict)

    print('Finished processing all records!!!')


if __name__ == '__main__':
    main()
