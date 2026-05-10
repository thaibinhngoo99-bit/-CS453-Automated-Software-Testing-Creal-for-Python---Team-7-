def this_conf_will_generate_for_this_pr(git_object, config):
    """Try to guess if this PR has a chance to generate something for this conf.

    Right now, just match the language in the conf with the presence
    of ONLY "readme.language.md" files.
    """
    lang = get_language_from_conf(config)
    filenames = [file.filename.lower() for file in get_files(git_object)]
    readme_lang = [name for name in filenames if re.match('(.*)readme.\\w+.md', name)]
    if len(readme_lang) != len(filenames):
        return True
    return bool([name for name in readme_lang if name.endswith('readme.{}.md'.format(lang))])