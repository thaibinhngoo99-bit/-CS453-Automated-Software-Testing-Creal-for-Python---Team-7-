def add_ycmd_debug_args(ycmd_process_handle, log_level='info', stdout_file_name=None, stderr_file_name=None, keep_logfiles=False):
    """
    Adds startup flags to `ycmd_process_handle` to enable logging output.

    The `ycmd_process_handle` should be an instance of `Process`.

    The `log_level` should be one of 'debug', 'info', 'warning', 'error', or
    'critical'. Any `str` is accepted, this routine does not actually check it.

    If `stdout_file_name` and `stderr_file_name` are provided, the server will
    write log messages to the given files. The bulk of the logs will be on
    stderr, with only a few startup messages appearing on stdout.

    If `keep_logfiles` is `True`, then the server won't delete the log files
    when it exits. Otherwise, the log files will be deleted when it shuts down.
    """
    if not isinstance(ycmd_process_handle, Process):
        raise TypeError('ycmd process handle must be a Process: %r' % ycmd_process_handle)
    assert isinstance(ycmd_process_handle, Process)
    if ycmd_process_handle.alive():
        raise ValueError('ycmd process is already started, cannot modify it: %r' % ycmd_process_handle)
    if not _is_valid_log_level(log_level):
        logger.warning('log level unrecognized: %r', log_level)
    ycmd_debug_args = ['--log=%s' % log_level]
    if stdout_file_name and stderr_file_name:
        ycmd_debug_args.extend(['--stdout=%s' % stdout_file_name, '--stderr=%s' % stderr_file_name])
        if keep_logfiles:
            ycmd_debug_args.append('--keep_logfiles')
    logger.debug('adding ycmd debug args: %r', ycmd_debug_args)
    ycmd_process_handle.args.extend(ycmd_debug_args)