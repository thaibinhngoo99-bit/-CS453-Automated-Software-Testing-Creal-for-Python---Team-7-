def new_tmp_file():
    """ Return a path to a new temporary file. """
    tmp_file, tmp_path = tempfile.mkstemp()
    os.close(tmp_file)
    TMP_FILES.append(tmp_path)
    return tmp_path