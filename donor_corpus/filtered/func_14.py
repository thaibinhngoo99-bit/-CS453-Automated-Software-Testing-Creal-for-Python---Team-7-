def check_config(reporter, source_dir):
    """Check configuration file."""
    config_file = os.path.join(source_dir, '_config.yml')
    config = load_yaml(config_file)
    reporter.check_field(config_file, 'configuration', config, 'kind', 'lesson')
    reporter.check_field(config_file, 'configuration', config, 'carpentry', ('swc', 'dc', 'lc', 'cp'))
    reporter.check_field(config_file, 'configuration', config, 'title')
    reporter.check_field(config_file, 'configuration', config, 'email')
    for defaults in [{'values': {'root': '.', 'layout': 'page'}}, {'values': {'root': '..', 'layout': 'episode'}, 'scope': {'type': 'episodes', 'path': ''}}, {'values': {'root': '..', 'layout': 'page'}, 'scope': {'type': 'extras', 'path': ''}}]:
        reporter.check(defaults in config.get('defaults', []), 'configuration', '"root" not set to "." in configuration')