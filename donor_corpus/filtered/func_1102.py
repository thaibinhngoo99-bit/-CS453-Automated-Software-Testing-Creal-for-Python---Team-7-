def synchronized(lock=None):
    """
    Synchronization decorator as described in
    http://blog.dscpl.com.au/2014/01/the-missing-synchronized-decorator.html.
    """

    def _decorator(wrapped):

        @functools.wraps(wrapped)
        def _wrapper(*args, **kwargs):
            with lock:
                return wrapped(*args, **kwargs)
        return _wrapper
    return _decorator