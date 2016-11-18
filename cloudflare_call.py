from __future__ import absolute_import
from __future__ import print_function
import CloudFlare


def cloudflare_details():
    cloudflare_details_params = {}
    cloudflare_details_params['cf'] = _connect()
    cloudflare_details_params['zone_info_dict'] = _get_zone_info(
        cloudflare_details_params['cf'])

    return cloudflare_details_params


def _connect():
    cf = CloudFlare.CloudFlare(raw=True)
    return cf


def _get_zone_info(cf):
    response = cf.zones.get(params={'per_page': 50})
    total_pages = response['result_info']['total_pages']
    page = 0
    zones = []
    zone_info_dict = {}

    while page <= total_pages:
        page += 1
        response = cf.zones.get(params={'page': page, 'per_page': 50})
        zones.extend(response['result'])

    for zone in zones:
        zone_info_dict[zone['name']] = zone['id']

    return zone_info_dict
