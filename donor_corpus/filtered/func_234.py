def _convertToPx(value):
    matched = re.match('(\\d+(?:\\.\\d+)?)?([a-z]*)$', value)
    if not matched:
        raise ValueError('unknown length value: %s' % value)
    length, unit = matched.groups()
    if unit == '':
        return float(length)
    elif unit == 'cm':
        return float(length) * 96 / 2.54
    elif unit == 'mm':
        return float(length) * 96 / 2.54 / 10
    elif unit == 'in':
        return float(length) * 96
    elif unit == 'pc':
        return float(length) * 96 / 6
    elif unit == 'pt':
        return float(length) * 96 / 6
    elif unit == 'px':
        return float(length)
    raise ValueError('unknown unit type: %s' % unit)