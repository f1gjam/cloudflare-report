from __future__ import absolute_import
from __future__ import print_function

import time


def countdown_time(time_in_seconds):
    # print('Waiting for few minutes so
    # that we don\'t hit the API Rate Limit \n')
    while time_in_seconds:
        mins, secs = divmod(time_in_seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        time_in_seconds -= 1
    print('Finished waiting for API limit cooldown timer!\n\n\n\n\n')
