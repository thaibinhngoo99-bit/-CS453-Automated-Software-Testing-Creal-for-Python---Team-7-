def save_file(file, content, append=False):
    mode = 'a' if append else 'w+'
    if not isinstance(content, six.string_types):
        mode = mode + 'b'
    with open(file, mode) as f:
        f.write(content)
        f.flush()