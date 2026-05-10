def gen_one_exception_builtin_entry(cw, exception, parent):
    exception.BeginSilverlight(cw)
    cw.enter_block('public static PythonType %s' % (exception.name,))
    if exception.fields:
        cw.write('get { return %s; }' % (exception.InternalPythonType,))
    else:
        cw.write('get { return %s; }' % (exception.InternalPythonType,))
    cw.exit_block()
    exception.EndSilverlight(cw)
    for child in exception.subclasses:
        gen_one_exception_builtin_entry(cw, child, exception)