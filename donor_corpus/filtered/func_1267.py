@pytest.fixture(autouse=True)
def skip_by_device_type(request, use_gpu, instance_type, accelerator_type):
    is_gpu = use_gpu or instance_type[3] in ['g', 'p']
    is_eia = accelerator_type is not None
    if request.node.get_closest_marker('gpu_test') and (not is_gpu) or (request.node.get_closest_marker('cpu_test') and is_gpu):
        pytest.skip("Skipping because running on '{}' instance".format(instance_type))
    elif (request.node.get_closest_marker('gpu_test') or request.node.get_closest_marker('cpu_test')) and is_eia:
        pytest.skip("Skipping because running on '{}' instance".format(instance_type))
    elif request.node.get_closest_marker('eia_test') and (not is_eia):
        pytest.skip("Skipping because running on '{}' instance".format(instance_type))