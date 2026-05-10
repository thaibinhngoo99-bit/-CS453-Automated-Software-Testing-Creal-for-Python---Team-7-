def getobjs(s):
    objs = []
    fs = os.listdir(s)
    for f in fs:
        absf = os.path.join(s, f)
        if os.path.isfile(absf) and os.path.splitext(f)[1] == '.py':
            objs.append(absf)
        elif os.path.isdir(absf):
            objs += getobjs(absf)
    return objs