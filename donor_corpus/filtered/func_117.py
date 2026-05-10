def gen_topython_helper(cw):
    cw.enter_block('private static BaseException/*!*/ ToPythonHelper(System.Exception clrException)')
    allExceps = get_all_exceps([], exceptionHierarchy)
    allExceps.sort(cmp=compare_exceptions)
    for x in allExceps[:-1]:
        if not x.silverlightSupported:
            cw.writeline('#if !SILVERLIGHT')
        cw.writeline('if (clrException is %s) return %s;' % (x.ExceptionMappingName, x.MakeNewException()))
        if not x.silverlightSupported:
            cw.writeline('#endif')
    cw.writeline('return new BaseException(Exception);')
    cw.exit_block()