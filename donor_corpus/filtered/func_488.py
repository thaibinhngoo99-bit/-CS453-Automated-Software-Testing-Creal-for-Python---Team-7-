def ListDirectory(directory, return_dotfiles=False):
    """Returns a list of files in dir.

  As with the standard os.listdir(), the filenames in the returned list will be
  the basenames of the files in dir (not absolute paths).  To get a list of
  absolute paths of files in a directory, a client could do:
    file_list = gfile.ListDir(my_dir)
    file_list = [os.path.join(my_dir, f) for f in file_list]
  (assuming that my_dir itself specified an absolute path to a directory).

  Args:
    directory: the directory to list
    return_dotfiles: if True, dotfiles will be returned as well.  Even if
      this arg is True, '.' and '..' will not be returned.

  Returns:
    ['list', 'of', 'files']. The entries '.' and '..' are never returned.
    Other entries starting with a dot will only be returned if return_dotfiles
    is True.
  Raises:
    OSError: if there is an error retrieving the directory listing.
  """
    files = os.listdir(directory)
    if not return_dotfiles:
        files = [f for f in files if not f.startswith('.')]
    return files