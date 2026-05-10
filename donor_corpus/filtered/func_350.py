@register_vcs_handler('git', 'get_keywords')
def git_get_keywords(versionfile_abs):
    """Extract version information from the given file."""
    keywords = {}
    try:
        f = open(versionfile_abs, 'r')
        for line in f.readlines():
            if line.strip().startswith('git_refnames ='):
                mo = re.search('=\\s*"(.*)"', line)
                if mo:
                    keywords['refnames'] = mo.group(1)
            if line.strip().startswith('git_full ='):
                mo = re.search('=\\s*"(.*)"', line)
                if mo:
                    keywords['full'] = mo.group(1)
            if line.strip().startswith('git_date ='):
                mo = re.search('=\\s*"(.*)"', line)
                if mo:
                    keywords['date'] = mo.group(1)
        f.close()
    except EnvironmentError:
        pass
    return keywords