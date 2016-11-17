from cloudflare_create_report import create_report


def test_create_report():
    filter_list_dict = [{
        '3plogistics.metapack.com': {
            'content': 'dm.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': '3c1130e10d3f7186291344c9a02278cf'
        }
    }, {
        'adamesh.metapack.com': {
            'content': 'dm.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': '40f96a78014a0805e1bd002a474930a2'
        }
    }, {
        'advancedsupplychain-uat.metapack.com': {
            'content': 'dm-delta.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': 'e78842c9444215a7205c8e728963b641'
        }
    }, {
        'aesop.metapack.com': {
            'content': 'dm.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': '97d5eb34f605033cdf4848cf1a72715e'
        }
    }, {
        'afrotherapy.metapack.com': {
            'content': 'dm.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': 'f6071a9d15fdd362146a059907929234'
        }
    }, {
        'airbornefootwear.metapack.com': {
            'content': 'dm.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': 'e0892db889cf9ae29f683803eec0dea7'
        }
    }, {
        'ajvanishoes.metapack.com': {
            'content': 'dm.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': '2220901ef6bf6261e4419b931f6e5b29'
        }
    }, {
        'alans.metapack.com': {
            'content': 'dm.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': '8a2ff4e42c70bad91dd3f4c222f317c6'
        }
    }, {
        'alexandalexa.metapack.com': {
            'content': 'dm.metapack.com',
            'proxiable': True,
            'ttl': 1,
            'type': 'CNAME',
            'proxied': True,
            'id': 'ebc053e5a8ec5fcc858901fd8dff192f'
        }
    }]

    report_dict_result = {
        '3plogistics.metapack.com': 'dm.metapack.com',
        'adamesh.metapack.com': 'dm.metapack.com',
        'advancedsupplychain-uat.metapack.com': 'dm-delta.metapack.com',
        'aesop.metapack.com': 'dm.metapack.com',
        'afrotherapy.metapack.com': 'dm.metapack.com',
        'airbornefootwear.metapack.com': 'dm.metapack.com',
        'ajvanishoes.metapack.com': 'dm.metapack.com',
        'alans.metapack.com': 'dm.metapack.com',
        'alexandalexa.metapack.com': 'dm.metapack.com'
    }

    assert create_report(filter_list_dict) == report_dict_result
