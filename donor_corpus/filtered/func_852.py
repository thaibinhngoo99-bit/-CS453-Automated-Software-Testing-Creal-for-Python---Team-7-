def test_rules_config_update(setup_scopez_server_action):
    """
    update rules config 0050-ZrLf3KKq.rules.json - change 
    user agent to Donkeez from Monkeez
    """
    l_uri = G_TEST_HOST
    l_headers = {'host': 'monkeez.com', 'user-agent': 'monkeez', 'waf-scopes-id': '0050'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is rules custom response\n'
    l_conf = {}
    l_file_path = os.path.dirname(os.path.abspath(__file__))
    l_rules_conf_path = os.path.realpath(os.path.join(l_file_path, '../../data/waf/conf/rules/0050-ZrLf3KkQ.rules.json'))
    try:
        with open(l_rules_conf_path) as l_f:
            l_conf = json.load(l_f)
    except Exception as l_e:
        print('error opening config file: %s.  Reason: %s error: %s, doc: %s' % (l_file_path, type(l_e), l_e, l_e.__doc__))
        assert False
    l_conf['directive'][1]['sec_rule']['operator']['value'] = 'donkeez'
    l_conf['last_modified_date'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    l_url = '%s/update_rules' % G_TEST_HOST
    l_headers = {'Content-Type': 'application/json', 'waf-scopes-id': '0050'}
    l_r = requests.post(l_url, headers=l_headers, data=json.dumps(l_conf))
    assert l_r.status_code == 200
    l_uri = G_TEST_HOST
    l_headers = {'host': 'monkeez.com', 'user-agent': 'monkeez', 'waf-scopes-id': '0050'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 200
    l_uri = G_TEST_HOST
    l_headers = {'host': 'monkeez.com', 'user-agent': 'donkeez', 'waf-scopes-id': '0050'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is rules custom response\n'