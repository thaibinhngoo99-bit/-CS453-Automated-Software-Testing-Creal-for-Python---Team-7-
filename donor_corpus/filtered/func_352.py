@register_vcs_handler('git', 'pieces_from_vcs')
def git_pieces_from_vcs(tag_prefix, root, verbose, run_command=run_command):
    """Get version from 'git describe' in the root of the source tree.

    This only gets called if the git-archive 'subst' keywords were *not*
    expanded, and _version.py hasn't already been rewritten with a short
    version string, meaning we're inside a checked out source tree.
    """
    GITS = ['git']
    if sys.platform == 'win32':
        GITS = ['git.cmd', 'git.exe']
    out, rc = run_command(GITS, ['rev-parse', '--git-dir'], cwd=root, hide_stderr=True)
    if rc != 0:
        if verbose:
            print('Directory %s not under git control' % root)
        raise NotThisMethod("'git rev-parse --git-dir' returned error")
    describe_out, rc = run_command(GITS, ['describe', '--tags', '--dirty', '--always', '--long', '--match', '%s*' % tag_prefix], cwd=root)
    if describe_out is None:
        raise NotThisMethod("'git describe' failed")
    describe_out = describe_out.strip()
    full_out, rc = run_command(GITS, ['rev-parse', 'HEAD'], cwd=root)
    if full_out is None:
        raise NotThisMethod("'git rev-parse' failed")
    full_out = full_out.strip()
    pieces = {}
    pieces['long'] = full_out
    pieces['short'] = full_out[:7]
    pieces['error'] = None
    git_describe = describe_out
    dirty = git_describe.endswith('-dirty')
    pieces['dirty'] = dirty
    if dirty:
        git_describe = git_describe[:git_describe.rindex('-dirty')]
    if '-' in git_describe:
        mo = re.search('^(.+)-(\\d+)-g([0-9a-f]+)$', git_describe)
        if not mo:
            pieces['error'] = "unable to parse git-describe output: '%s'" % describe_out
            return pieces
        full_tag = mo.group(1)
        if not full_tag.startswith(tag_prefix):
            if verbose:
                fmt = "tag '%s' doesn't start with prefix '%s'"
                print(fmt % (full_tag, tag_prefix))
            pieces['error'] = "tag '%s' doesn't start with prefix '%s'" % (full_tag, tag_prefix)
            return pieces
        pieces['closest-tag'] = full_tag[len(tag_prefix):]
        pieces['distance'] = int(mo.group(2))
        pieces['short'] = mo.group(3)
    else:
        pieces['closest-tag'] = None
        count_out, rc = run_command(GITS, ['rev-list', 'HEAD', '--count'], cwd=root)
        pieces['distance'] = int(count_out)
    date = run_command(GITS, ['show', '-s', '--format=%ci', 'HEAD'], cwd=root)[0].strip()
    pieces['date'] = date.strip().replace(' ', 'T', 1).replace(' ', '', 1)
    return pieces