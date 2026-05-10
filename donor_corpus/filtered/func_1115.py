def rm_rf(path):
    """
    Recursively removes a file or directory
    """
    if not path or not os.path.exists(path):
        return
    if is_alpine():
        try:
            return run('rm -rf "%s"' % path)
        except Exception:
            pass
    chmod_r(path, 511)
    exists_but_non_dir = os.path.exists(path) and (not os.path.isdir(path))
    if os.path.isfile(path) or exists_but_non_dir:
        os.remove(path)
    else:
        shutil.rmtree(path)