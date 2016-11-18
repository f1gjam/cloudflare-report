from __future__ import absolute_import
from __future__ import print_function

import cloudflare_filter_records
import cloudflare_yaml_io


def main():

    domain = 'metapack.com'
    stack_list = ['dm', 'dm2', 'dm3',  'dm4',  'dm5',  'dm6', ]
    zone_record_dict = cloudflare_yaml_io.read_yaml_backup_file()

    filter_list_dict = cloudflare_filter_records.filter_stack(
        zone_record_dict, domain , stack_list)

    print(filter_list_dict)

    print('Finished processing all records!!!')


if __name__ == '__main__':
    main()
