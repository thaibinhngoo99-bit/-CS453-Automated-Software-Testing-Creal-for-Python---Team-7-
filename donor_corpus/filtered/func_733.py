def get_imageId_from_fileName(filename, id_iter):
    """Get imageID from fileName if fileName is int, else return id_iter."""
    filename = os.path.splitext(filename)[0]
    if filename.isdigit():
        return int(filename)
    return id_iter