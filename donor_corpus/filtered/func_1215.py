def data():
    """Returns a dictionary with the static data on the images.

    The dictionary is read from a JSON file lazily the first time
    this function is called.
    """
    global _data
    if not _data:
        json_dir = os.path.abspath(os.path.dirname(__file__))
        json_file = os.path.join(json_dir, 'images.json')
        with open(json_file) as f:
            _data = json.load(f)
    return _data