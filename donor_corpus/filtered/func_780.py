def lookup(scopes, name):
    """Look up `name` in `scopes`."""
    for scope in scopes:
        for key, val in scope:
            if key == name:
                return val
    return None