from __future__ import absolute_import
from __future__ import print_function
import re
import yaml
import glob
import os


def read_yaml_backup_file():
    file_list = []
    zone_record_dict = {}
    os.chdir("/tmp")
    for file in glob.glob("cloudflare-backup-dns-*.yml"):
        file_list.append(file)

    for file in file_list:
        txt_filename = file

        re1 = '.*?'  # Non-greedy match on filler
        # File Name 1
        re2 = '((?:[a-z][a-z\\.\\d_]+)\\.(?:[a-z\\d]{3}))(?![\\w\\.])'

        rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
        m = rg.search(txt_filename)
        if m:
            file1 = m.group(1)
            domain = file1.split('.yml')

            zone_record_dict[domain[0]] = _yaml_load_all(txt_filename)
            print('Finished reading: ' + txt_filename)

    return zone_record_dict


def _yaml_load_all(filename):
    with open(filename, 'r') as ymlfile:
        return yaml.load(ymlfile)
