def fromtext(data, source_name=None):
    """Parse a Relay program."""
    if data == '':
        raise ParseError('Cannot parse the empty string.')
    global __source_name_counter__
    if source_name is None:
        source_name = 'source_file{0}'.format(__source_name_counter__)
    if isinstance(source_name, str):
        source_name = SourceName(source_name)
    tree = make_parser(data).prog()
    return ParseTreeToRelayIR(source_name).visit(tree)