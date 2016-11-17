from __future__ import absolute_import
from __future__ import print_function


def create_report(filter_list_dict):
    report_dict = {}
    for dict_item in filter_list_dict:
        for k, v in dict_item.iteritems():
            report_dict[k] = v['content']
    return report_dict
