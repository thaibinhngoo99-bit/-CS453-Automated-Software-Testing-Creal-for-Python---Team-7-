def Rename(oldpath, newpath, overwrite=False):
    """Rename or move a file, or a local directory.

  Args:
    oldpath: string; a pathname of a file.
    newpath: string; a pathname to which the file will be moved.
    overwrite: boolean; if false, it is an error for newpath to be
      occupied by an existing file.

  Raises:
    OSError: If "newpath" is occupied by an existing file and overwrite=False.
  """
    if not overwrite and Exists(newpath) and (not IsDirectory(newpath)):
        raise OSError(errno.EEXIST, os.strerror(errno.EEXIST), newpath)
    os.rename(oldpath, newpath)