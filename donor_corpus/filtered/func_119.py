def gen_one_exception_module_entry(cw, exception, parent):
    exception.BeginSilverlight(cw)
    cw.write('public static PythonType %s = %s;' % (exception.name, exception.InternalPythonType))
    exception.EndSilverlight(cw)
    for child in exception.subclasses:
        gen_one_exception_module_entry(cw, child, exception)