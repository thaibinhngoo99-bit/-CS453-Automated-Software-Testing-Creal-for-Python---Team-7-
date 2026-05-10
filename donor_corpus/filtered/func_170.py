def stringify(cobj, indent=2):
    s = '%s\n' % type(cobj)
    if issubclass(type(cobj), ctypes.Union):
        cobj = getattr(cobj, cobj._fields_[0][0])
    if issubclass(type(cobj), ctypes.Structure):
        for field in cobj._fields_:
            s += '%s%s=%s\n' % (indent * ' ', field[0], stringify(getattr(cobj, field[0]), indent + 2))
        return s
    try:
        return bytearray(cobj[:])
    except TypeError:
        return '%d (0x%x)' % (cobj, cobj)