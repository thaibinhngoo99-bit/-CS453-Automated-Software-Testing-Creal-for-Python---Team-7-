def __get_integration_config(client, integration_name, prints_manager, thread_index=0):
    body = {'page': 0, 'size': 100, 'query': 'name:' + integration_name}
    try:
        res_raw = demisto_client.generic_request_func(self=client, path='/settings/integration/search', method='POST', body=body)
    except ApiException as conn_error:
        prints_manager.add_print_job(conn_error, print, thread_index)
        return None
    res = ast.literal_eval(res_raw[0])
    TIMEOUT = 180
    SLEEP_INTERVAL = 5
    total_sleep = 0
    while 'configurations' not in res:
        if total_sleep == TIMEOUT:
            error_message = 'Timeout - failed to get integration {} configuration. Error: {}'.format(integration_name, res)
            prints_manager.add_print_job(error_message, print_error, thread_index)
            return None
        time.sleep(SLEEP_INTERVAL)
        total_sleep += SLEEP_INTERVAL
    all_configurations = res['configurations']
    match_configurations = [x for x in all_configurations if x['name'] == integration_name]
    if not match_configurations or len(match_configurations) == 0:
        prints_manager.add_print_job('integration was not found', print_error, thread_index)
        return None
    return match_configurations[0]