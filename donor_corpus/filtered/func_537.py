def _main():
    descr = 'Generate Gerrit release announcement email text'
    parser = argparse.ArgumentParser(description=descr, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--version', dest='version', required=True, help='gerrit version to release')
    parser.add_argument('-p', '--previous', dest='previous', help='previous gerrit version (optional)')
    parser.add_argument('-s', '--summary', dest='summary', help='summary of the release content (optional)')
    options = parser.parse_args()
    summary = options.summary
    if summary and (not summary.endswith('.')):
        summary = summary + '.'
    data = {'version': Version(options.version), 'previous': options.previous, 'summary': summary}
    war = os.path.join(os.path.expanduser('~/.m2/repository/com/google/gerrit/gerrit-war/'), '%(version)s/gerrit-war-%(version)s.war' % data)
    if not os.path.isfile(war):
        print('Could not find war file for Gerrit %s in local Maven repository' % data['version'], file=sys.stderr)
        sys.exit(1)
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    BUF_SIZE = 65536
    with open(war, 'rb') as f:
        while True:
            d = f.read(BUF_SIZE)
            if not d:
                break
            md5.update(d)
            sha1.update(d)
            sha256.update(d)
    data['sha1'] = sha1.hexdigest()
    data['sha256'] = sha256.hexdigest()
    data['md5'] = md5.hexdigest()
    template = Template(open('tools/release-announcement-template.txt').read())
    output = template.render(data=data)
    filename = 'release-announcement-gerrit-%s.txt' % data['version']
    with open(filename, 'w') as f:
        f.write(output)
    gpghome = os.path.abspath(os.path.expanduser('~/.gnupg'))
    if not os.path.isdir(gpghome):
        print('Skipping signing due to missing gnupg home folder')
    else:
        try:
            gpg = GPG(homedir=gpghome)
        except TypeError:
            gpg = GPG(gnupghome=gpghome)
        signed = gpg.sign(output)
        filename = filename + '.asc'
        with open(filename, 'w') as f:
            f.write(str(signed))