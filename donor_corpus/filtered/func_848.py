def define_function(name, text):
    lines = []
    lines.append('function ' + name + '() {')
    for line_ in text.splitlines():
        lines.append('  ' + line_)
    lines.append('}')
    return '\n'.join(lines)