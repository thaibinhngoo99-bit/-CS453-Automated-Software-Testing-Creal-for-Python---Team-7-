def spanify(f):
    """A decorator which attaches span information
       to the value returned by calling `f`.

       Intended for use with the below AST visiting
       methods. The idea is that after we do the work
       of constructing the AST we attach Span information.
    """

    def _wrapper(*args, **kwargs):
        sn = args[0].source_name
        ctx = args[1]
        ast = f(*args, **kwargs)
        line, col = ctx.getSourceInterval()
        sp = Span(sn, line, col)
        if isinstance(ast, tvm.relay.expr.TupleWrapper):
            ast = ast.astuple()
        ast.set_span(sp)
        return ast
    return _wrapper