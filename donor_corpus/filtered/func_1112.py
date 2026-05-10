def obj_to_xml(obj):
    """ Return an XML representation of the given object (dict, list, or primitive).
        Does NOT add a common root element if the given obj is a list.
        Does NOT work for nested dict structures. """
    if isinstance(obj, list):
        return ''.join([obj_to_xml(o) for o in obj])
    if isinstance(obj, dict):
        return ''.join(['<{k}>{v}</{k}>'.format(k=k, v=obj_to_xml(v)) for k, v in obj.items()])
    return str(obj)