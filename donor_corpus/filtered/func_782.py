def make_parser(data):
    """Construct a RelayParser a given data stream."""
    input_stream = InputStream(data)
    lexer = RelayLexer(input_stream)
    lexer.addErrorListener(StrictErrorListener(data))
    token_stream = CommonTokenStream(lexer)
    p = RelayParser(token_stream)
    p.addErrorListener(StrictErrorListener(data))
    return p