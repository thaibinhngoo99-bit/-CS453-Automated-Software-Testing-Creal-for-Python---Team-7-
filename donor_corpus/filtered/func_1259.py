@nox.session
def check_lower_bounds(session):
    """Check lower bounds in setup.py are reflected in constraints file"""
    session.install('google-cloud-testutils')
    session.install('.')
    session.run('lower-bound-checker', 'check', '--package-name', PACKAGE_NAME, '--constraints-file', str(LOWER_BOUND_CONSTRAINTS_FILE))