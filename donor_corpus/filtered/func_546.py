def __create_integration_instance(client, integration_name, integration_instance_name, integration_params, is_byoi, prints_manager, validate_test=True, thread_index=0):
    start_message = 'Configuring instance for {} (instance name: {}, validate "Test": {})'.format(integration_name, integration_instance_name, validate_test)
    prints_manager.add_print_job(start_message, print, thread_index)
    configuration = __get_integration_config(client, integration_name, prints_manager, thread_index=thread_index)
    if not configuration:
        return (None, 'No configuration', None)
    module_configuration = configuration['configuration']
    if not module_configuration:
        module_configuration = []
    instance_name = '{}_test_{}'.format(integration_instance_name.replace(' ', '_'), str(uuid.uuid4()))
    module_instance = {'brand': configuration['name'], 'category': configuration['category'], 'configuration': configuration, 'data': [], 'enabled': 'true', 'engine': '', 'id': '', 'isIntegrationScript': is_byoi, 'name': instance_name, 'passwordProtected': False, 'version': 0}
    for param_conf in module_configuration:
        if param_conf['display'] in integration_params or param_conf['name'] in integration_params:
            key = param_conf['display'] if param_conf['display'] in integration_params else param_conf['name']
            if key == 'credentials':
                credentials = integration_params[key]
                param_value = {'credential': '', 'identifier': credentials['identifier'], 'password': credentials['password'], 'passwordChanged': False}
            else:
                param_value = integration_params[key]
            param_conf['value'] = param_value
            param_conf['hasvalue'] = True
        elif param_conf['defaultValue']:
            param_conf['value'] = param_conf['defaultValue']
        module_instance['data'].append(param_conf)
    try:
        res = demisto_client.generic_request_func(self=client, method='PUT', path='/settings/integration', body=module_instance)
    except ApiException as conn_err:
        error_message = 'Error trying to create instance for integration: {0}:\n {1}'.format(integration_name, conn_err)
        prints_manager.add_print_job(error_message, print_error, thread_index)
        return (None, error_message, None)
    if res[1] != 200:
        error_message = 'create instance failed with status code ' + str(res[1])
        prints_manager.add_print_job(error_message, print_error, thread_index)
        prints_manager.add_print_job(pformat(res[0]), print_error, thread_index)
        return (None, error_message, None)
    integration_config = ast.literal_eval(res[0])
    module_instance['id'] = integration_config['id']
    if validate_test:
        test_succeed, failure_message = __test_integration_instance(client, module_instance, prints_manager, thread_index=thread_index)
    else:
        print_warning('Skipping test validation for integration: {} (it has test_validate set to false)'.format(integration_name))
        test_succeed = True
    if not test_succeed:
        __disable_integrations_instances(client, [module_instance], prints_manager, thread_index=thread_index)
        return (None, failure_message, None)
    docker_image = Docker.get_integration_image(integration_config)
    return (module_instance, '', docker_image)