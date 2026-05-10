def check_source_rmd(reporter, source_dir, parser):
    """Check that Rmd episode files include `source: Rmd`"""
    episode_rmd_dir = [os.path.join(source_dir, d) for d in SOURCE_RMD_DIRS]
    episode_rmd_files = [os.path.join(d, '*.Rmd') for d in episode_rmd_dir]
    results = {}
    for pat in episode_rmd_files:
        for f in glob.glob(pat):
            data = read_markdown(parser, f)
            dy = data['metadata']
            if dy:
                reporter.check_field(f, 'episode_rmd', dy, 'source', 'Rmd')