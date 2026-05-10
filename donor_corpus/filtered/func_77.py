def to_startup_parameters(ycmd_root_directory, ycmd_settings_path=None, working_directory=None, python_binary_path=None, server_idle_suicide_seconds=None, server_check_interval_seconds=None):
    """
    Internal convenience function. Receives the raw arguments to starting a
    ycmd server and returns a `StartupParameters` instance from it.

    If the first argument is already `StartupParameters`, it is returned as-is,
    and the remaining parameters are ignored.

    Otherwise, a `StartupParameters` instance is constructed with all the given
    parameters and returned.
    """
    if isinstance(ycmd_root_directory, StartupParameters):
        if ycmd_settings_path is not None:
            logger.warning('ycmd settings path will be ignored: %s', ycmd_settings_path)
        if working_directory is not None:
            logger.warning('working directory will be ignored: %s', working_directory)
        if python_binary_path is not None:
            logger.warning('python binary path will be ignored: %s', python_binary_path)
        if server_idle_suicide_seconds is not None:
            logger.warning('server idle suicide seconds will be ignored: %s', server_idle_suicide_seconds)
        if server_check_interval_seconds is not None:
            logger.warning('server check interval seconds will be ignored: %s', server_check_interval_seconds)
        return ycmd_root_directory
    logger.warning('[DEPRECATED] to startup parameters', stack_info=True)
    logger.debug('generating startup parameters with root: %s', ycmd_root_directory)
    return StartupParameters(ycmd_root_directory, ycmd_settings_path=ycmd_settings_path, working_directory=working_directory, python_binary_path=python_binary_path, server_idle_suicide_seconds=server_idle_suicide_seconds, server_check_interval_seconds=server_check_interval_seconds)