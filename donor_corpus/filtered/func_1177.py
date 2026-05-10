@contextmanager
def cloud_storage_http_request(method, url, max_retries=5, backoff_factor=2, retry_codes=_TRANSIENT_FAILURE_RESPONSE_CODES, timeout=None, **kwargs):
    """
    Performs an HTTP PUT/GET request using Python's `requests` module with automatic retry.

    :param method: string of 'PUT' or 'GET', specify to do http PUT or GET
    :param url: the target URL address for the HTTP request.
    :param max_retries: maximum number of retries before throwing an exception.
    :param backoff_factor: a time factor for exponential backoff. e.g. value 5 means the HTTP
      request will be retried with interval 5, 10, 20... seconds. A value of 0 turns off the
      exponential backoff.
    :param retry_codes: a list of HTTP response error codes that qualifies for retry.
    :param timeout: wait for timeout seconds for response from remote server for connect and
      read request. Default to None owing to long duration operation in read / write.
    :param kwargs: Additional keyword arguments to pass to `requests.Session.request()`

    :return requests.Response object.
    """
    if method.lower() not in ('put', 'get'):
        raise ValueError('Illegal http method: ' + method)
    try:
        with _get_http_response_with_retries(method, url, max_retries, backoff_factor, retry_codes, timeout=timeout, **kwargs) as response:
            yield response
    except Exception as e:
        raise MlflowException('API request failed with exception %s' % e)