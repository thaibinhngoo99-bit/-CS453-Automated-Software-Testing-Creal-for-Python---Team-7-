def get_context_tag_from_file_list(files_list):
    context_tags = set()
    for filename in files_list:
        filepath = Path(filename)
        filename = filepath.as_posix()
        if '/examples/' in filename:
            continue
        match = re.match('specification/(.*)/Microsoft.\\w*/(stable|preview)/', filename, re.I)
        if match:
            context_tags.add(match.groups()[0])
            continue
        match = re.match('specification/(.*)/(stable|preview)/', filename, re.I)
        if match:
            context_tags.add(match.groups()[0])
            continue
        match = re.match('specification/(.*)/readme.\\w*.?md', filename, re.I)
        if match:
            context_tags.add(match.groups()[0])
            continue
    return context_tags