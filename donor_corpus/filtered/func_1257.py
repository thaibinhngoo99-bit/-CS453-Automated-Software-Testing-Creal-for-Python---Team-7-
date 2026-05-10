@nox.session(python=['3.6', '3.7'])
def mypy(session):
    """Run the type checker."""
    session.install('mypy', 'types-pkg_resources')
    session.install('.')
    session.run('mypy', '--explicit-package-bases', 'google')