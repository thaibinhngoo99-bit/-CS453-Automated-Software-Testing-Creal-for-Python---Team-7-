@nox.session
def update_lower_bounds(session):
    """Update lower bounds in constraints.txt to match setup.py"""
    session.install('google-cloud-testutils')
    session.install('.')
    session.run('lower-bound-checker', 'update', '--package-name', PACKAGE_NAME, '--constraints-file', str(LOWER_BOUND_CONSTRAINTS_FILE))