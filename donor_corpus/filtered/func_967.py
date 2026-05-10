def _is_inventory_group(key, value):
    """
    Verify that a module-level variable (key = value) is a valid inventory group.
    """
    if key.startswith('_') or not isinstance(value, (list, tuple, GeneratorType)):
        return False
    if isinstance(value, tuple):
        value = value[0]
    if isinstance(value, GeneratorType):
        value = list(value)
    return all((isinstance(item, ALLOWED_HOST_TYPES) for item in value))