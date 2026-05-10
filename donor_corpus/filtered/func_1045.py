def solve_relative_path(autorest_options, sdk_root):
    """Solve relative path in conf.

    If a key is prefixed by "sdkrel:", it's solved against SDK root.
    """
    SDKRELKEY = 'sdkrel:'
    solved_autorest_options = {}
    for key, value in autorest_options.items():
        if key.startswith(SDKRELKEY):
            _LOGGER.debug('Found a sdkrel pair: %s/%s', key, value)
            subkey = key[len(SDKRELKEY):]
            solved_value = Path(sdk_root, value).resolve()
            solved_autorest_options[subkey] = str(solved_value)
        else:
            solved_autorest_options[key] = value
    return solved_autorest_options