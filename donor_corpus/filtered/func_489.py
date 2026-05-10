def Stat(path):
    """Gets the status of a file.

  Args:
    path: The file to call Stat() on.

  Does the equivalent of Stat() on the specified "path" and return file
  properties.

  Returns:
    An object whose attributes give information on the file.

  Raises:
    OSError: If "path" does not exist.
  """
    statinfo = os.stat(path)
    filestat = collections.namedtuple('FileStat', ['mtime'])
    filestat.mtime = statinfo.st_mtime
    return filestat