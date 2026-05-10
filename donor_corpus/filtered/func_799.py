def process_varargs(varargs: list, b_map: dict):
    """
    wrapper around process_request that returns legacy values to preserve backward compatibility
    :param varargs: a list with the path to the file requested.
    :param b_map: bucket map
    :return: path, bucket, object_name
    """
    log.warning('Deprecated process_varargs() called.')
    path, bucket, object_name, _ = process_request(varargs, b_map)
    return (path, bucket, object_name)