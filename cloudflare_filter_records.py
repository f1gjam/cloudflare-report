from __future__ import absolute_import
from __future__ import print_function

import re
import sys


def filter_stack(zone_record_dict, domain, stack):
    filter_list_dict = []
    if domain == 'all':
        print('Not supporting ALL domains currently')
        sys.exit(1)
    else:
        if domain in zone_record_dict:
            for record in zone_record_dict[domain]:
                for k in record:
                    content = record[k]['content']
                    if stack == 'dm':
                        x = 'dm[^\d]'
                        if re.search(x, content, re.IGNORECASE) and \
                                record[k]['type'] == 'CNAME' and \
                                re.search(domain, content, re.IGNORECASE):
                            filter_list_dict.append(record)
                    else:
                        if re.search(stack, content, re.IGNORECASE) \
                                and record[k]['type'] == 'CNAME' and \
                                re.search(domain, content, re.IGNORECASE):
                            filter_list_dict.append(record)
            return filter_list_dict

        else:
            print('domain or stack not found')
