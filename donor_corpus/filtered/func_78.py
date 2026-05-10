def check_startup_parameters(startup_parameters):
    """
    Performs quick, non-blocking validation on startup parameters to catch type
    mismatches or empty configurations. Raises an exception or returns `None`.

    This is meant to be run on the main thread to catch common startup errors
    before initializing the server off-thread. It isn't strictly necessary, but
    produces nicer error messages when the plugin is not configured correctly.

    NOTE : This does not check the file system for things like missing files,
           as that can be a blocking operation.
    """
    if not isinstance(startup_parameters, StartupParameters):
        raise TypeError('startup parameters must be StartupParameters: %r' % startup_parameters)
    ycmd_root_directory = startup_parameters.ycmd_root_directory
    if not ycmd_root_directory:
        raise RuntimeError('no ycmd root directory has been set')
    ycmd_settings_path = startup_parameters.ycmd_settings_path
    if not ycmd_settings_path:
        raise RuntimeError('no ycmd default settings path has been set')
    logger.debug('startup parameters seem to be filled in, ready to attempt startup: %r', startup_parameters)