def parseargs(string: str):
    """Split a given string into individual arguments, seperated into key:arg for <key>=(' or ")<arg>(same char as start)"""
    arg = {}
    parts = string.split(' ')
    bkey = ''
    buffer = ''
    end = '"'
    for part in parts:
        if '=' in part:
            key, vp = part.split('=')
            if vp[0] in ('"', "'"):
                end = vp[0]
            if vp.endswith(end):
                arg[key] = vp[1:-1]
            else:
                bkey = key
                buffer += vp
        elif part.endswith(end):
            buffer += ' ' + part
            arg[bkey] = buffer[1:-1]
            bkey, buffer = ('', '')
        else:
            buffer += ' ' + part
    return arg