def is_string(s, include_unicode=True, exclude_binary=False):
    if isinstance(s, six.binary_type) and exclude_binary:
        return False
    if isinstance(s, str):
        return True
    if include_unicode and isinstance(s, six.text_type):
        return True
    return False