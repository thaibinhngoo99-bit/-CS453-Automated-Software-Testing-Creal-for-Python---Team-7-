def get_readme_files_from_file_list(files_list, base_dir=Path('.')):
    """Get readme files from this PR.
    Algo is to look for context, and then search for Readme inside this context.
    """
    readme_files = set()
    context_tags = get_context_tag_from_file_list(files_list)
    for context_tag in context_tags:
        expected_folder = Path(base_dir) / Path('specification/{}'.format(context_tag))
        if not expected_folder.is_dir():
            _LOGGER.warning("From context {} I didn't find folder {}".format(context_tag, expected_folder))
            continue
        for expected_readme in [l for l in expected_folder.iterdir() if l.is_file()]:
            match = re.match('readme.\\w*.?md', expected_readme.name, re.I)
            if match:
                readme_files.add(expected_readme.relative_to(Path(base_dir)))
    return readme_files