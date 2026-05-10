def wait_for_port_open(port, http_path=None, expect_success=True, retries=10, sleep_time=0.5):
    """ Ping the given network port until it becomes available (for a given number of retries).
        If 'http_path' is set, make a GET request to this path and assert a non-error response. """

    def check():
        if not is_port_open(port, http_path=http_path, expect_success=expect_success):
            raise Exception()
    return retry(check, sleep=sleep_time, retries=retries)