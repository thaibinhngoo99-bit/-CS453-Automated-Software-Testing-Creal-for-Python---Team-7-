def read_all_markdown(source_dir, parser):
    """Read source files, returning
    {path : {'metadata':yaml, 'metadata_len':N, 'text':text, 'lines':[(i, line, len)], 'doc':doc}}
    """
    all_dirs = [os.path.join(source_dir, d) for d in SOURCE_DIRS]
    all_patterns = [os.path.join(d, '*.md') for d in all_dirs]
    result = {}
    for pat in all_patterns:
        for filename in glob.glob(pat):
            data = read_markdown(parser, filename)
            if data:
                result[filename] = data
    return result