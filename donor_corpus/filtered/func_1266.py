@pytest.fixture(name='instance_type', scope='session')
def fixture_instance_type(request, processor):
    provided_instance_type = request.config.getoption('--instance-type')
    default_instance_type = 'local' if processor == 'cpu' else 'local_gpu'
    return provided_instance_type or default_instance_type