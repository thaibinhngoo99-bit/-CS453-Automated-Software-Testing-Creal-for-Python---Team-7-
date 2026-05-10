def get_type(name):
    if name.startswith('IronPython'):
        return ip.GetType(name)
    if name.startswith('Microsoft.Scripting'):
        res = ms.GetType(name)
        return res if res is not None else md.GetType(name)
    if name.startswith('System.ComponentModel'):
        return sysdll.GetType(name)
    return System.Type.GetType(name)