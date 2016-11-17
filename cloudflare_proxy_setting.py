from __future__ import absolute_import
from __future__ import print_function

import datetime

import cloudflare_timer

# Global Variables
max_requests = 800
api_sleep_time_in_seconds = 320


def get_record_info(cloudflare_details_params, filtered_dict, cli_arg_params):
    cf = cloudflare_details_params['cf']

    zone_info_dict = cloudflare_details_params['zone_info_dict']
    set_flag = cli_arg_params['flag']
    domain_zone = cli_arg_params['domain']
    total_records = len(filtered_dict)

    print('Total records: ' + str(total_records))
    count = 0
    start_time = datetime.datetime.now()

    for record in filtered_dict:
        for k, v in record.iteritems():
            fqdn = k
            single_record_values = v
            count += 1

            current_time = datetime.datetime.now()
            duration = (current_time - start_time)
            if count >= max_requests or duration.seconds >= 240:
                cloudflare_timer.countdown_time(api_sleep_time_in_seconds)
                count = 0  # reset count
                start_time = datetime.datetime.now()  # reset start_time
                print('counter/start_time reset')
            else:
                _set_proxy(
                    cf,
                    zone_info_dict,
                    set_flag,
                    domain_zone,
                    fqdn,
                    single_record_values)


def _set_proxy(cf, zone_info_dict, set_flag,
               domain_zone, fqdn, single_record_values):
    if set_flag is True:
        # Disable proxy ONLY for records which have proxy
        # Enabled currently - if records have proxy
        # enabled already skip them (as per backup
        # configuration being read
        if single_record_values['proxiable'] and single_record_values[
                'proxied'] is True:
            print('Disabling Proxy for: ' +
                  fqdn +
                  ' current value: ' +
                  str(single_record_values['proxied']))

            single_record_values['proxied'] = False
            _proxy_setting(
                cf, zone_info_dict[domain_zone], fqdn, single_record_values)
        else:
            print(
                'Cannot set Proxy for: ' +
                fqdn +
                ' not proxiable! or already disabled')
    elif set_flag is False:
        # Disable proxy ONLY for records who's backup
        # configuration states it should be disabled
        if single_record_values['proxiable']:
            print('Reseting Proxy for: ' +
                  fqdn +
                  ' to original value: ' +
                  str(single_record_values['proxied']))
            _proxy_setting(
                cf, zone_info_dict[domain_zone], fqdn, single_record_values)
        else:
            print(
                'Cannot set Proxy for: ' +
                fqdn +
                ' not proxiable!')


def _proxy_setting(cf, zone_id, fqdn, single_record_values):
    dns_record = {
        'zone_id': zone_id,
        'id': single_record_values['id'],
        'proxied': single_record_values['proxied'],
        'type': single_record_values['type'],
        'name': fqdn,
        'content': single_record_values['content'],
        'ttl': single_record_values['ttl']
    }

    response = cf.zones.dns_records.put(
        zone_id, single_record_values['id'], data=dns_record)
    return response
