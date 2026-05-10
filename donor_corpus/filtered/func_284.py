def write_log(string, prefix, **kwargs):
    """Write the data to logging info."""
    prefix = prefix
    logging.info(prefix)
    string = string
    logging.info(string)