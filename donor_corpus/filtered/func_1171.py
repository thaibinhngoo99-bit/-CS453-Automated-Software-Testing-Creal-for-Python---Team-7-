def http_request(host_creds, endpoint, method, max_retries=5, backoff_factor=2, retry_codes=_TRANSIENT_FAILURE_RESPONSE_CODES, timeout=120, **kwargs):
    """
    Makes an HTTP request with the specified method to the specified hostname/endpoint. Transient
    errors such as Rate-limited (429), service unavailable (503) and internal error (500) are
    retried with an exponential back off with backoff_factor * (1, 2, 4, ... seconds).
    The function parses the API response (assumed to be JSON) into a Python object and returns it.

    :param host_creds: A :py:class:`mlflow.rest_utils.MlflowHostCreds` object containing
        hostname and optional authentication.
    :param endpoint: a string for service endpoint, e.g. "/path/to/object".
    :param method: a string indicating the method to use, e.g. "GET", "POST", "PUT".
    :param max_retries: maximum number of retries before throwing an exception.
    :param backoff_factor: a time factor for exponential backoff. e.g. value 5 means the HTTP
      request will be retried with interval 5, 10, 20... seconds. A value of 0 turns off the
      exponential backoff.
    :param retry_codes: a list of HTTP response error codes that qualifies for retry.
    :param timeout: wait for timeout seconds for response from remote server for connect and
      read request.
    :param kwargs: Additional keyword arguments to pass to `requests.Session.request()`

    :return: requests.Response object.
    """
    hostname = host_creds.host
    auth_str = None
    if host_creds.username and host_creds.password:
        basic_auth_str = ('%s:%s' % (host_creds.username, host_creds.password)).encode('utf-8')
        auth_str = 'Basic ' + base64.standard_b64encode(basic_auth_str).decode('utf-8')
    elif host_creds.token:
        auth_str = 'Bearer %s' % host_creds.token
    from mlflow.tracking.request_header.registry import resolve_request_headers
    headers = dict({**_DEFAULT_HEADERS, **resolve_request_headers()})
    if auth_str:
        headers['Authorization'] = auth_str
    if host_creds.server_cert_path is None:
        verify = not host_creds.ignore_tls_verification
    else:
        verify = host_creds.server_cert_path
    if host_creds.client_cert_path is not None:
        kwargs['cert'] = host_creds.client_cert_path
    cleaned_hostname = strip_suffix(hostname, '/')
    url = '%s%s' % (cleaned_hostname, endpoint)
    try:
        return _get_http_response_with_retries(method, url, max_retries, backoff_factor, retry_codes, headers=headers, verify=verify, timeout=timeout, **kwargs)
    except Exception as e:
        raise MlflowException('API request to %s failed with exception %s' % (url, e))