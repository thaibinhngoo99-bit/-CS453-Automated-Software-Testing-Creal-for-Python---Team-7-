def _convert_to_numeric(s):
    if 'M' in s:
        s = s.strip('M')
        return force_float(s) * 1000000
    if 'B' in s:
        s = s.strip('B')
        return force_float(s) * 1000000000
    return force_float(s)