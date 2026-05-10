def convert_paramILS_to_HCBR_params(paramILS):
    convert_map = {'e': 'eta', 'd': 'delta', 'g': 'gamma', 'i': 'online', 'p': 'learning_phases', 'z': 'heuristic'}

    def if_exists(k, v):
        if k in convert_map:
            return (convert_map[k], v)
        else:
            return (None, None)
    params = {}
    for k, v in paramILS.iteritems():
        key, val = if_exists(k, v)
        if key is not None:
            params[key] = val
    return params