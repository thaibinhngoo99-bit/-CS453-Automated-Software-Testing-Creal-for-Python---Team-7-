def get_input_paths(global_conf, local_conf):
    """Returns a 2-tuple:
    - Markdown Path or None
    - Input-file Paths or empty list
    """
    del global_conf
    relative_markdown_path = None
    input_files = []
    if 'markdown' in local_conf:
        relative_markdown_path = Path(local_conf['markdown'])
    input_files = local_conf.get('autorest_options', {}).get('input-file', [])
    if input_files and (not isinstance(input_files, list)):
        input_files = [input_files]
    input_files = [Path(input_file) for input_file in input_files]
    if not relative_markdown_path and (not input_files):
        raise ValueError('No input file found')
    return (relative_markdown_path, input_files)