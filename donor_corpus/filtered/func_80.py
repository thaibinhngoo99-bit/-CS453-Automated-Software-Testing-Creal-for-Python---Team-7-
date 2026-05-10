def prepare_ycmd_process(startup_parameters, ycmd_settings_tempfile_path, ycmd_server_hostname, ycmd_server_port):
    """
    Initializes and returns a `Process` handle, correctly configured to launch
    a ycmd server process. It does not automatically start it though.
    The `ycmd_settings_tempfile_path` should be created by (return value of)
    `write_ycmd_settings_file`. The ycmd server process will read that file on
    startup and then immediately delete it.
    The `ycmd_server_hostname` and `ycmd_server_port` must also be provided to
    instruct the server to listen on the given address.
    """
    assert isinstance(startup_parameters, StartupParameters), 'startup parameters must be StartupParameters: %r' % startup_parameters
    assert isinstance(ycmd_settings_tempfile_path, str), 'ycmd settings temporary file path must be a str: %r' % ycmd_settings_tempfile_path
    check_startup_parameters(startup_parameters)
    working_directory = startup_parameters.working_directory
    python_binary_path = startup_parameters.python_binary_path
    server_idle_suicide_seconds = startup_parameters.server_idle_suicide_seconds
    server_check_interval_seconds = startup_parameters.server_check_interval_seconds
    ycmd_module_directory = startup_parameters.ycmd_module_directory
    if YCMD_LOG_SPOOL_OUTPUT:
        stdout_log_spool = tempfile.SpooledTemporaryFile(max_size=YCMD_LOG_SPOOL_SIZE)
        stderr_log_spool = tempfile.SpooledTemporaryFile(max_size=YCMD_LOG_SPOOL_SIZE)
        logger.debug('using temporary spools for stdout, stderr: %r, %r', stdout_log_spool, stderr_log_spool)
        stdout_handle = stdout_log_spool
        stderr_handle = stderr_log_spool
    else:
        stdout_handle = FileHandles.DEVNULL
        stderr_handle = FileHandles.DEVNULL
    ycmd_process_handle = Process()
    ycmd_process_handle.binary = python_binary_path
    ycmd_process_handle.args.extend([ycmd_module_directory, '--host=%s' % ycmd_server_hostname, '--port=%s' % ycmd_server_port, '--idle_suicide_seconds=%s' % server_idle_suicide_seconds, '--check_interval_seconds=%s' % server_check_interval_seconds, '--options_file=%s' % ycmd_settings_tempfile_path])
    ycmd_process_handle.cwd = working_directory
    ycmd_process_handle.filehandles.stdout = stdout_handle
    ycmd_process_handle.filehandles.stderr = stderr_handle
    if startup_parameters.log_level is not None:
        add_ycmd_debug_args(ycmd_process_handle, log_level=startup_parameters.log_level, stdout_file_name=startup_parameters.stdout_log_path, stderr_file_name=startup_parameters.stderr_log_path, keep_logfiles=startup_parameters.keep_logs)
    return ycmd_process_handle