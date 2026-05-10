@nox.session(python='3.6')
def docs(session):
    """Build the docs for this library."""
    session.install('-e', '.')
    session.install('sphinx<3.0.0', 'alabaster', 'recommonmark')
    shutil.rmtree(os.path.join('docs', '_build'), ignore_errors=True)
    session.run('sphinx-build', '-W', '-T', '-N', '-b', 'html', '-d', os.path.join('docs', '_build', 'doctrees', ''), os.path.join('docs', ''), os.path.join('docs', '_build', 'html', ''))