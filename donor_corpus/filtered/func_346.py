def get_config():
    """Create, populate and return the VersioneerConfig() object."""
    cfg = VersioneerConfig()
    cfg.VCS = 'git'
    cfg.style = 'pep440'
    cfg.tag_prefix = 'v'
    cfg.parentdir_prefix = 'psyplot-ci-release-test-'
    cfg.versionfile_source = 'release_test/_version.py'
    cfg.verbose = False
    return cfg