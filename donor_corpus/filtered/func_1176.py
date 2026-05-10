def call_endpoint(host_creds, endpoint, method, json_body, response_proto):
    if json_body:
        json_body = json.loads(json_body)
    if method == 'GET':
        response = http_request(host_creds=host_creds, endpoint=endpoint, method=method, params=json_body)
    else:
        response = http_request(host_creds=host_creds, endpoint=endpoint, method=method, json=json_body)
    response = verify_rest_response(response, endpoint)
    js_dict = json.loads(response.text)
    parse_dict(js_dict=js_dict, message=response_proto)
    return response_proto