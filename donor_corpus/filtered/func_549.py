def __delete_integration_instance(client, instance_id, prints_manager, thread_index=0):
    try:
        res = demisto_client.generic_request_func(self=client, method='DELETE', path='/settings/integration/' + urllib.quote(instance_id))
    except requests.exceptions.RequestException as conn_err:
        error_message = 'Failed to delete integration instance, error trying to communicate with demisto server: {} '.format(conn_err)
        prints_manager.add_print_job(error_message, print_error, thread_index)
        return False
    if int(res[1]) != 200:
        error_message = 'delete integration instance failed\nStatus code' + str(res[1])
        prints_manager.add_print_job(error_message, print_error, thread_index)
        prints_manager.add_print_job(pformat(res), print_error, thread_index)
        return False
    return True