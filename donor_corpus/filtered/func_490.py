def Copy(oldpath, newpath, overwrite=False):
    """Copy a file.

  Args:
    oldpath: string; a pathname of a file.
    newpath: string; a pathname to which the file will be copied.
    overwrite: boolean; if false, it is an error for newpath to be
      occupied by an existing file.

  Raises:
    OSError: If "newpath" is occupied by an existing file and overwrite=False,
             or any error thrown by shutil.copy.
  """
    if not overwrite and Exists(newpath):
        raise OSError(errno.EEXIST, os.strerror(errno.EEXIST), newpath)
    shutil.copy(oldpath, newpath)