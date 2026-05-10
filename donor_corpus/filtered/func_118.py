def gen_one_exception(cw, e):
    supername = getattr(exceptions, e).__bases__[0].__name__
    if not supername in pythonExcs and supername != 'Warning':
        supername = ''
    cw.write(CLASS1, name=get_clr_name(e), supername=get_clr_name(supername), make_new_exception=get_exception_info(e, exceptionHierarchy).MakeNewException())