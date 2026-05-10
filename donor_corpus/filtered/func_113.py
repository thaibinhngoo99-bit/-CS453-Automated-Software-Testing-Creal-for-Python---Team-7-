def get_all_exceps(l, curHierarchy):
    for exception in curHierarchy.subclasses:
        found = False
        for e in l:
            if e.clrException == exception.clrException:
                found = True
                break
        if not found:
            l.append(exception)
    for exception in curHierarchy.subclasses:
        get_all_exceps(l, exception)
    return l