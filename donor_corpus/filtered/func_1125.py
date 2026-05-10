def unzip(path, target_dir, overwrite=True):
    if is_alpine():
        flags = '-o' if overwrite else ''
        return run('cd %s; unzip %s %s' % (target_dir, flags, path))
    try:
        zip_ref = zipfile.ZipFile(path, 'r')
    except Exception as e:
        LOG.warning('Unable to open zip file: %s: %s' % (path, e))
        raise e
    try:
        for file_entry in zip_ref.infolist():
            _unzip_file_entry(zip_ref, file_entry, target_dir)
    finally:
        zip_ref.close()