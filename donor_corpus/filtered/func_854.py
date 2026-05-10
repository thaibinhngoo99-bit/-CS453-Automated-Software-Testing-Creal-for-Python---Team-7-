def test_limit_config_update(setup_scopez_server_action):
    l_uri = G_TEST_HOST + '/test.html'
    l_headers = {'host': 'limit.com', 'waf-scopes-id': '0050'}
    for _ in range(2):
        l_r = requests.get(l_uri, headers=l_headers)
        assert l_r.status_code == 200
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is ddos custom response\n'
    l_uri = G_TEST_HOST + '/test.html'
    l_headers = {'host': 'test.limit.com', 'waf-scopes-id': '0050'}
    for _ in range(2):
        l_r = requests.get(l_uri, headers=l_headers)
        assert l_r.status_code == 200
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'custom response for limits from limit_id_2\n'
    time.sleep(2)
    l_conf = {}
    l_file_path = os.path.dirname(os.path.abspath(__file__))
    l_limit_conf_path = os.path.realpath(os.path.join(l_file_path, '../../data/waf/conf/limit/0050-MjMhNXMR.limit.json'))
    try:
        with open(l_limit_conf_path) as l_f:
            l_conf = json.load(l_f)
    except Exception as l_e:
        print('error opening config file: %s.  Reason: %s error: %s, doc: %s' % (l_limit_conf_path, type(l_e), l_e, l_e.__doc__))
        assert False
    l_conf['num'] = 3
    l_conf['last_modified_date'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    l_url = '%s/update_limit' % G_TEST_HOST
    l_headers = {'Content-Type': 'application/json', 'waf-scopes-id': '0050'}
    l_r = requests.post(l_url, headers=l_headers, data=json.dumps(l_conf))
    assert l_r.status_code == 200
    l_uri = G_TEST_HOST + '/test.html'
    l_headers = {'host': 'limit.com', 'waf-scopes-id': '0050'}
    for _ in range(3):
        l_r = requests.get(l_uri, headers=l_headers)
        assert l_r.status_code == 200
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is ddos custom response\n'
    l_uri = G_TEST_HOST + '/test.html'
    l_headers = {'host': 'test.limit.com', 'waf-scopes-id': '0050'}
    for _ in range(3):
        l_r = requests.get(l_uri, headers=l_headers)
        assert l_r.status_code == 200
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'custom response for limits from limit_id_2\n'