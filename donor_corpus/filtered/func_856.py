def test_scopes_linkage_update(setup_scopez_server_action):
    """
    Test linkage update. Update rules config in second scope
    (0050-scopes.json) to 0050-0gG8osWJ.rules.json from
    0050-ZrLf3KkQ.rules.json check if update worked
    """
    l_uri = G_TEST_HOST + '/path.html'
    l_headers = {'host': 'test.com', 'waf-scopes-id': '0050', 'User-Agent': 'monkeez'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is rules custom response\n'
    l_conf = {}
    l_file_path = os.path.dirname(os.path.abspath(__file__))
    l_scopes_conf_path = os.path.realpath(os.path.join(l_file_path, '../../data/waf/conf/scopes/0050.scopes.json'))
    try:
        with open(l_scopes_conf_path) as l_f:
            l_conf = json.load(l_f)
    except Exception as l_e:
        print('error opening config file: %s.  Reason: %s error: %s, doc: %s' % (l_scopes_conf_path, type(l_e), l_e, l_e.__doc__))
        assert False
    l_conf['scopes'][1]['rules_prod_id'] = '0gG8osWJ'
    l_conf['last_modified_date'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    l_url = '%s/update_scopes' % G_TEST_HOST
    l_headers = {'Content-Type': 'application/json'}
    l_r = requests.post(l_url, headers=l_headers, data=json.dumps(l_conf))
    assert l_r.status_code == 200
    l_uri = G_TEST_HOST + '/path.html'
    l_headers = {'host': 'test.com', 'waf-scopes-id': '0050', 'User-Agent': 'monkeez'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 200
    l_uri = G_TEST_HOST + '/path.html'
    l_headers = {'host': 'test.com', 'waf-scopes-id': '0050', 'User-Agent': 'bananas'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is rules custom response\n'