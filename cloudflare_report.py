from __future__ import absolute_import
from __future__ import print_function

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> parent of 02fe446... removed cloudflare_call which isn't needed by this script, this is because all of the information it needs is within the backup file.
import cloudflare_call
import cloudflare_cli
>>>>>>> parent of 02fe446... removed cloudflare_call which isn't needed by this script, this is because all of the information it needs is within the backup file.
import cloudflare_filter_records
import cloudflare_yaml_io


def main():
<<<<<<< HEAD
=======
    cli_arg_params = cloudflare_cli.cli_args()

    cloudflare_details_params = cloudflare_call.cloudflare_details()
<<<<<<< HEAD
>>>>>>> parent of 02fe446... removed cloudflare_call which isn't needed by this script, this is because all of the information it needs is within the backup file.
=======
>>>>>>> parent of 02fe446... removed cloudflare_call which isn't needed by this script, this is because all of the information it needs is within the backup file.

    domain = 'metapack.com'
    stack_list = ['dm', 'dm2', 'dm3',  'dm4',  'dm5',  'dm6', ]
    zone_record_dict = cloudflare_yaml_io.read_yaml_backup_file()

    filter_list_dict = cloudflare_filter_records.filter_stack(
<<<<<<< HEAD
        zone_record_dict, domain , stack_list)
=======
        zone_record_dict, cli_arg_params['domain'], cli_arg_params['stack'])

    # cloudflare_proxy_setting.get_record_info(cloudflare_details_params,
    #                                         filter_list_dict, cli_arg_params)
<<<<<<< HEAD
>>>>>>> parent of 02fe446... removed cloudflare_call which isn't needed by this script, this is because all of the information it needs is within the backup file.
=======
>>>>>>> parent of 02fe446... removed cloudflare_call which isn't needed by this script, this is because all of the information it needs is within the backup file.

    print(filter_list_dict)

    print('Finished processing all records!!!')


if __name__ == '__main__':
    main()
