def debug_print(enabled_or_option='debug'):
    """Get a debug printer that is enabled based on a boolean input or a pyglet option.
    The debug print function returned should be used in an assert. This way it can be
    optimized out when running python with the -O flag.

    Usage example::

        from pyglet.debug import debug_print
        _debug_media = debug_print('debug_media')

        def some_func():
            assert _debug_media('My debug statement')

    :parameters:
        `enabled_or_options` : bool or str
            If a bool is passed, debug printing is enabled if it is True. If str is passed
            debug printing is enabled if the pyglet option with that name is True.

    :returns: Function for debug printing.
    """
    if isinstance(enabled_or_option, bool):
        enabled = enabled_or_option
    else:
        enabled = pyglet.options.get(enabled_or_option, False)
    if enabled:

        def _debug_print(*args, **kwargs):
            print(*args, **kwargs)
            return True
    else:

        def _debug_print(*args, **kwargs):
            return True
    return _debug_print