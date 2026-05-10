def _is_valid_log_level(log_level):
    if not isinstance(log_level, str):
        raise TypeError('log level must be a str: %r' % log_level)
    recognized_log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    return log_level in recognized_log_levels