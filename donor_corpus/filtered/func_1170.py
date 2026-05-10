def _get_http_response_with_retries(method, url, max_retries, backoff_factor, retry_codes, **kwargs):
    """
    Performs an HTTP request using Python's `requests` module with an automatic retry policy.

    :param method: a string indicating the method to use, e.g. "GET", "POST", "PUT".
    :param url: the target URL address for the HTTP request.
    :param max_retries: Maximum total number of retries.
    :param backoff_factor: a time factor for exponential backoff. e.g. value 5 means the HTTP
      request will be retried with interval 5, 10, 20... seconds. A value of 0 turns off the
      exponential backoff.
    :param retry_codes: a list of HTTP response error codes that qualifies for retry.
    :param kwargs: Additional keyword arguments to pass to `requests.Session.request()`

    :return: requests.Response object.
    """
    assert 0 <= max_retries < 10
    assert 0 <= backoff_factor < 120
    retry_kwargs = {'total': max_retries, 'connect': max_retries, 'read': max_retries, 'redirect': max_retries, 'status': max_retries, 'status_forcelist': retry_codes, 'backoff_factor': backoff_factor}
    if Version(urllib3.__version__) >= Version('1.26.0'):
        retry_kwargs['allowed_methods'] = None
    else:
        retry_kwargs['method_whitelist'] = None
    retry = Retry(**retry_kwargs)
    adapter = HTTPAdapter(max_retries=retry)
    with requests.Session() as http:
        http.mount('https://', adapter)
        http.mount('http://', adapter)
        response = http.request(method, url, **kwargs)
        return response