@nox.session(python=['3.6', '3.7', '3.8', '3.9'])
def unit(session):
    """Run the unit test suite."""
    session.install('coverage', 'pytest', 'pytest-cov', 'asyncmock', 'pytest-asyncio')
    session.install('-e', '.')
    session.run('py.test', '--quiet', '--cov=google/cloud/asset_v1p4beta1/', '--cov-config=.coveragerc', '--cov-report=term', '--cov-report=html', os.path.join('tests', 'unit', ''.join(session.posargs)))