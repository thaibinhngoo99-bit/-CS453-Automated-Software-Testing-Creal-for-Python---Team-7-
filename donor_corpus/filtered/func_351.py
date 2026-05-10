@register_vcs_handler('git', 'keywords')
def git_versions_from_keywords(keywords, tag_prefix, verbose):
    """Get version information from git keywords."""
    if not keywords:
        raise NotThisMethod('no keywords at all, weird')
    date = keywords.get('date')
    if date is not None:
        date = date.strip().replace(' ', 'T', 1).replace(' ', '', 1)
    refnames = keywords['refnames'].strip()
    if refnames.startswith('$Format'):
        if verbose:
            print('keywords are unexpanded, not using')
        raise NotThisMethod('unexpanded keywords, not a git-archive tarball')
    refs = set([r.strip() for r in refnames.strip('()').split(',')])
    TAG = 'tag: '
    tags = set([r[len(TAG):] for r in refs if r.startswith(TAG)])
    if not tags:
        tags = set([r for r in refs if re.search('\\d', r)])
        if verbose:
            print("discarding '%s', no digits" % ','.join(refs - tags))
    if verbose:
        print('likely tags: %s' % ','.join(sorted(tags)))
    for ref in sorted(tags):
        if ref.startswith(tag_prefix):
            r = ref[len(tag_prefix):]
            if verbose:
                print('picking %s' % r)
            return {'version': r, 'full-revisionid': keywords['full'].strip(), 'dirty': False, 'error': None, 'date': date}
    if verbose:
        print('no suitable tags, using unknown + full revision id')
    return {'version': '0+unknown', 'full-revisionid': keywords['full'].strip(), 'dirty': False, 'error': 'no suitable tags', 'date': None}