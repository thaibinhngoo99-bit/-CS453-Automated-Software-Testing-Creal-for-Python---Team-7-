def verify_rest_response(response, endpoint):
    """Verify the return code and format, raise exception if the request was not successful."""
    if response.status_code != 200:
        if _can_parse_as_json(response.text):
            raise RestException(json.loads(response.text))
        else:
            base_msg = 'API request to endpoint %s failed with error code %s != 200' % (endpoint, response.status_code)
            raise MlflowException("%s. Response body: '%s'" % (base_msg, response.text))
    if endpoint.startswith(_REST_API_PATH_PREFIX) and (not _can_parse_as_json(response.text)):
        base_msg = 'API request to endpoint was successful but the response body was not in a valid JSON format'
        raise MlflowException("%s. Response body: '%s'" % (base_msg, response.text))
    return response