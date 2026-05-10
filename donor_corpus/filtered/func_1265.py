@pytest.fixture(scope='session', name='build_base_image', autouse=True)
def fixture_build_base_image(request, framework_version, py_version, processor, tag, docker_base_name):
    build_base_image = request.config.getoption('--build-base-image')
    if build_base_image:
        return image_utils.build_base_image(framework_name=docker_base_name, framework_version=framework_version, py_version=py_version, base_image_tag=tag, processor=processor, cwd=os.path.join(dir_path, '..'))
    return tag