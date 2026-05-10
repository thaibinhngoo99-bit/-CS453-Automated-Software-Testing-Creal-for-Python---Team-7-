def __delete_incident(client, incident, prints_manager, thread_index=0):
    try:
        body = {'ids': [incident['id']], 'filter': {}, 'all': False}
        res = demisto_client.generic_request_func(self=client, method='POST', path='/incident/batchDelete', body=body)
    except requests.exceptions.RequestException as conn_err:
        error_message = 'Failed to delete incident, error trying to communicate with demisto server: {} '.format(conn_err)
        prints_manager.add_print_job(error_message, print_error, thread_index)
        return False
    if int(res[1]) != 200:
        error_message = 'delete incident failed\nStatus code' + str(res[1])
        prints_manager.add_print_job(error_message, print_error, thread_index)
        prints_manager.add_print_job(pformat(res), print_error, thread_index)
        return False
    return True