def test_scopes_update(setup_scopez_server_action):
    l_uri = G_TEST_HOST + '/path.html'
    l_headers = {'host': 'www.regexhost.com', 'waf-scopes-id': '0051', 'User-Agent': 'bananas'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is from RX scope\n'
    l_conf = {}
    l_file_path = os.path.dirname(os.path.abspath(__file__))
    l_scopes_conf_path = os.path.realpath(os.path.join(l_file_path, '../../data/waf/conf/scopes/0051.scopes.json'))
    try:
        with open(l_scopes_conf_path) as l_f:
            l_conf = json.load(l_f)
    except Exception as l_e:
        print('error opening config file: %s.  Reason: %s error: %s, doc: %s' % (l_scopes_conf_path, type(l_e), l_e, l_e.__doc__))
        assert False
    l_conf['scopes'][1]['path']['value'] = '.*/test.html'
    l_conf['last_modified_date'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    l_url = '%s/update_scopes' % G_TEST_HOST
    l_headers = {'Content-Type': 'application/json'}
    l_r = requests.post(l_url, headers=l_headers, data=json.dumps(l_conf))
    assert l_r.status_code == 200
    l_uri = G_TEST_HOST + '/path.html'
    l_headers = {'host': 'www.regexhost.com', 'waf-scopes-id': '0051', 'User-Agent': 'bananas'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is from GLOB scope\n'
    l_uri = G_TEST_HOST + '/test.html'
    l_headers = {'host': 'www.regexhost.com', 'waf-scopes-id': '0051', 'User-Agent': 'bananas'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is from RX scope\n'