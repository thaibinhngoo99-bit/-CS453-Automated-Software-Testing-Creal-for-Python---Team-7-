def get_language_from_conf(meta_conf):
    """Detect the language based on the default Autorest options.
    Assuming all language use --mylanguage in the config file.
    If I don't find anything, well just say I don't know...

    This is based on autorest language flags.
    :rtype: Language
    """
    autorest_options_lang = set(meta_conf['autorest_options'].keys())
    languages = set()
    for value in Language:
        if value in autorest_options_lang:
            languages.add(value)
    if not languages:
        _LOGGER.warning('No detected language from this conf')
        return None
    language = languages.pop()
    if languages:
        _LOGGER.warning("This SwaggerToSdk conf seems to generate too much language in one call, assume we don't know")
        return None
    return language