def test_profile_config_update(setup_scopez_server_action):
    """
    update profile config 0050-YrLf3KkQ.wafprof.json - change
    ignore_query_args to test from ignore
    """
    l_uri = G_TEST_HOST + '/profile.html?a=%27select%20*%20from%20testing%27'
    l_headers = {'host': 'monkeez.com', 'waf-scopes-id': '0050'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is profile custom response\n'
    l_uri = G_TEST_HOST + '/profile.html?ignore=%27select%20*%20from%20testing%27'
    l_headers = {'host': 'monkeez.com', 'waf-scopes-id': '0050'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 200
    l_conf = {}
    l_file_path = os.path.dirname(os.path.abspath(__file__))
    l_profile_conf_path = os.path.realpath(os.path.join(l_file_path, '../../data/waf/conf/profile/0050-YrLf3KkQ.wafprof.json'))
    try:
        with open(l_profile_conf_path) as l_f:
            l_conf = json.load(l_f)
    except Exception as l_e:
        print('error opening config file: %s.  Reason: %s error: %s, doc: %s' % (l_profile_conf_path, type(l_e), l_e, l_e.__doc__))
        assert False
    l_conf['general_settings']['ignore_query_args'] = ['test']
    l_conf['last_modified_date'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    l_url = '%s/update_profile' % G_TEST_HOST
    l_headers = {'Content-Type': 'application/json', 'waf-scopes-id': '0050'}
    l_r = requests.post(l_url, headers=l_headers, data=json.dumps(l_conf))
    assert l_r.status_code == 200
    l_uri = G_TEST_HOST + '/profile.html?ignore=%27select%20*%20from%20testing%27'
    l_headers = {'host': 'monkeez.com', 'waf-scopes-id': '0050'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 403
    assert l_r.text == 'This is profile custom response\n'
    l_uri = G_TEST_HOST + '/profile.html?test=%27select%20*%20from%20testing%27'
    l_headers = {'host': 'monkeez.com', 'waf-scopes-id': '0050'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 200