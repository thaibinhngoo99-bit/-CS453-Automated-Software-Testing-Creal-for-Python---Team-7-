def write_ycmd_settings_file(ycmd_settings_path, ycmd_hmac_secret, out=None):
    """
    Writes out a ycmd server settings file based on the template file
    `ycmd_settings_path`. A uniquely-generated `ycmd_hmac_secret` must also be
    supplied, as it needs to be written into this file.
    The return value is the path to the settings file, as a `str`.
    If `out` is omitted, a secure temporary file is created, and the returned
    path should be passed via the options flag to ycmd.
    If `out` is provided, it should be a path to an output file (`str`), or a
    file-like handle (must support `.write`). This is not recommended for use
    with ycmd, as it may be insecure.
    """
    ycmd_settings_data = generate_settings_data(ycmd_settings_path, ycmd_hmac_secret)
    out_path = None
    if out is None:
        temp_file_object = tempfile.NamedTemporaryFile(prefix='ycmd_settings_', suffix='.json', delete=False)
        temp_file_name = temp_file_object.name
        temp_file_handle = temp_file_object.file
        out = temp_file_handle
        out_path = temp_file_name

        def flush():
            temp_file_handle.flush()

        def close():
            temp_file_object.close()
    else:
        raise NotImplementedError('unimplemented: output to specific file')
    if out_path is None and out is not None:
        logger.error('failed to get path for output file: %r', out)
    save_json_file(out, ycmd_settings_data)
    flush()
    close()
    logger.debug('successfully wrote file: %s', out_path)
    return out_path