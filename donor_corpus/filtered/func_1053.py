def _prepare_docstring(value):
    if not value:
        return ''
    remove_spaces = 0
    for line in value.split('\n')[1:]:
        if line:
            for char in line:
                if char != ' ':
                    break
                else:
                    remove_spaces += 1
            break
    return re.sub('^ {%s}' % remove_spaces, '', unicode(value), flags=re.MULTILINE).strip()