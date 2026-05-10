def test_update_bots_endpoint(setup_scopez_server_action):
    l_url = G_TEST_HOST + '/update_bots'
    l_file_path = os.path.dirname(os.path.abspath(__file__))
    l_test_file = os.path.realpath(os.path.join(l_file_path, '../../data/waf/conf/bots/0052-wHyMHxV7.bots.json'))
    l_test_payload = ''
    assert os.path.exists(l_test_file), 'test file not found!'
    with open(l_test_file) as l_tf:
        l_test_payload = l_tf.read()
    assert l_test_payload, 'payload is empty!'
    l_json_payload = json.loads(l_test_payload)
    l_uri = G_TEST_HOST + '/test.html'
    l_headers = {'host': 'mybot.com', 'user-agent': 'bot-testing', 'waf-scopes-id': '0052'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 401
    l_json_payload['directive'][0]['sec_rule']['operator']['value'] = 'chowdah'
    l_json_payload['last_modified_date'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    l_result = requests.post(l_url, timeout=3, json=l_json_payload)
    assert l_result.status_code == 200
    assert l_result.json()['status'] == 'success'
    l_uri = G_TEST_HOST + '/test.html'
    l_headers = {'host': 'mybot.com', 'user-agent': 'bot-testing', 'waf-scopes-id': '0052'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 200, 'expecting 200, got {resp_code} since user-agent changed to chowdah'.format(resp_code=l_r.status_code)
    l_uri = G_TEST_HOST + '/test.html'
    l_headers = {'host': 'mybot.com', 'user-agent': 'chowdah', 'waf-scopes-id': '0052'}
    l_r = requests.get(l_uri, headers=l_headers)
    assert l_r.status_code == 401, 'expecting 401, got {resp_code} since user-agent changed to chowdah'.format(resp_code=l_r.status_code)
    l_cust_id = l_json_payload.pop('customer_id')
    l_n2_result = requests.post(l_url, json=l_json_payload)
    assert l_n2_result.status_code == 500, 'expected 500 since customer_id {} is removed'.format(l_cust_id)