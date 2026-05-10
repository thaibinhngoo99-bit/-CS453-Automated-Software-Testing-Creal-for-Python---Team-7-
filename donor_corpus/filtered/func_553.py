def disable_all_integrations(demisto_api_key, server, prints_manager, thread_index=0):
    """
    Disable all enabled integrations. Should be called at start of test loop to start out clean

    Arguments:
        client -- demisto py client
    """
    client = demisto_client.configure(base_url=server, api_key=demisto_api_key, verify_ssl=False)
    try:
        body = {'size': 1000}
        int_resp = demisto_client.generic_request_func(self=client, method='POST', path='/settings/integration/search', body=body)
        int_instances = ast.literal_eval(int_resp[0])
    except requests.exceptions.RequestException as conn_err:
        error_message = 'Failed to disable all integrations, error trying to communicate with demisto server: {} '.format(conn_err)
        prints_manager.add_print_job(error_message, print_error, thread_index)
        return
    if int(int_resp[1]) != 200:
        error_message = 'Get all integration instances failed with status code: {}'.format(int_resp[1])
        prints_manager.add_print_job(error_message, print_error, thread_index)
        return
    if 'instances' not in int_instances:
        prints_manager.add_print_job('No integrations instances found to disable all', print, thread_index)
        return
    to_disable = []
    for instance in int_instances['instances']:
        if instance.get('enabled') == 'true' and instance.get('isIntegrationScript'):
            add_to_disable_message = 'Adding to disable list. Name: {}. Brand: {}'.format(instance.get('name'), instance.get('brand'))
            prints_manager.add_print_job(add_to_disable_message, print, thread_index)
            to_disable.append(instance)
    if len(to_disable) > 0:
        __disable_integrations_instances(client, to_disable, prints_manager, thread_index=thread_index)