def test_integration(client, server_url, integrations, playbook_id, prints_manager, options=None, is_mock_run=False, thread_index=0):
    options = options if options is not None else {}
    module_instances = []
    test_docker_images = set()
    with open('./Tests/conf.json', 'r') as conf_file:
        docker_thresholds = json.load(conf_file).get('docker_thresholds', {}).get('images', {})
    for integration in integrations:
        integration_name = integration.get('name', None)
        integration_instance_name = integration.get('instance_name', '')
        integration_params = integration.get('params', None)
        is_byoi = integration.get('byoi', True)
        validate_test = integration.get('validate_test', True)
        if is_mock_run:
            configure_proxy_unsecure(integration_params)
        module_instance, failure_message, docker_image = __create_integration_instance(client, integration_name, integration_instance_name, integration_params, is_byoi, prints_manager, validate_test=validate_test, thread_index=thread_index)
        if module_instance is None:
            failure_message = failure_message if failure_message else 'No failure message could be found'
            msg = 'Failed to create instance: {}'.format(failure_message)
            prints_manager.add_print_job(msg, print_error, thread_index)
            __delete_integrations_instances(client, module_instances, prints_manager, thread_index=thread_index)
            return (False, -1)
        module_instances.append(module_instance)
        if docker_image:
            test_docker_images.update(docker_image)
        prints_manager.add_print_job('Create integration {} succeed'.format(integration_name), print, thread_index)
    incident, inc_id = __create_incident_with_playbook(client, 'inc_{}'.format(playbook_id), playbook_id, integrations, prints_manager, thread_index=thread_index)
    if not incident:
        return (False, -1)
    investigation_id = incident['investigationId']
    if investigation_id is None or len(investigation_id) == 0:
        incident_id_not_found_msg = 'Failed to get investigation id of incident:' + incident
        prints_manager.add_print_job(incident_id_not_found_msg, print_error, thread_index)
        return (False, -1)
    prints_manager.add_print_job('Investigation URL: {}/#/WorkPlan/{}'.format(server_url, investigation_id), print, thread_index)
    timeout_amount = options['timeout'] if 'timeout' in options else DEFAULT_TIMEOUT
    timeout = time.time() + timeout_amount
    i = 1
    while True:
        time.sleep(1)
        playbook_state = __get_investigation_playbook_state(client, investigation_id, prints_manager, thread_index=thread_index)
        if playbook_state in (PB_Status.COMPLETED, PB_Status.NOT_SUPPORTED_VERSION):
            break
        if playbook_state == PB_Status.FAILED:
            if is_mock_run:
                prints_manager.add_print_job(playbook_id + ' failed with error/s', print_warning, thread_index)
                __print_investigation_error(client, playbook_id, investigation_id, prints_manager, LOG_COLORS.YELLOW, thread_index=thread_index)
            else:
                prints_manager.add_print_job(playbook_id + ' failed with error/s', print_error, thread_index)
                __print_investigation_error(client, playbook_id, investigation_id, prints_manager, thread_index=thread_index)
            break
        if time.time() > timeout:
            prints_manager.add_print_job(playbook_id + ' failed on timeout', print_error, thread_index)
            break
        if i % DEFAULT_INTERVAL == 0:
            loop_number_message = 'loop no. {}, playbook state is {}'.format(i / DEFAULT_INTERVAL, playbook_state)
            prints_manager.add_print_job(loop_number_message, print, thread_index)
        i = i + 1
    __disable_integrations_instances(client, module_instances, prints_manager, thread_index=thread_index)
    if test_docker_images:
        memory_threshold = options.get('memory_threshold', Docker.DEFAULT_CONTAINER_MEMORY_USAGE)
        pids_threshold = options.get('pid_threshold', Docker.DEFAULT_CONTAINER_PIDS_USAGE)
        error_message = Docker.check_resource_usage(server_url=server_url, docker_images=test_docker_images, def_memory_threshold=memory_threshold, def_pid_threshold=pids_threshold, docker_thresholds=docker_thresholds)
        if error_message:
            prints_manager.add_print_job(error_message, print_error, thread_index)
            return (PB_Status.FAILED_DOCKER_TEST, inc_id)
    else:
        prints_manager.add_print_job('Skipping docker container memory resource check for test {}'.format(playbook_id), print_warning, thread_index)
    test_pass = playbook_state in (PB_Status.COMPLETED, PB_Status.NOT_SUPPORTED_VERSION)
    if test_pass:
        __delete_incident(client, incident, prints_manager, thread_index=thread_index)
        __delete_integrations_instances(client, module_instances, prints_manager, thread_index=thread_index)
    return (playbook_state, inc_id)