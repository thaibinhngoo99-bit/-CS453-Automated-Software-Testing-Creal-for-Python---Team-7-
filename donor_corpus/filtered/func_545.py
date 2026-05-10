def __test_integration_instance(client, module_instance, prints_manager, thread_index=0):
    connection_retries = 3
    response_code = 0
    prints_manager.add_print_job('trying to connect.', print_warning, thread_index)
    for i in range(connection_retries):
        try:
            response_data, response_code, _ = demisto_client.generic_request_func(self=client, method='POST', path='/settings/integration/test', body=module_instance, _request_timeout=120)
            break
        except ApiException as conn_err:
            error_msg = 'Failed to test integration instance, error trying to communicate with demisto server: {} '.format(conn_err)
            prints_manager.add_print_job(error_msg, print_error, thread_index)
            return (False, None)
        except urllib3.exceptions.ReadTimeoutError:
            warning_msg = 'Could not connect. Trying to connect for the {} time'.format(i + 1)
            prints_manager.add_print_job(warning_msg, print_warning, thread_index)
    if int(response_code) != 200:
        test_failed_msg = 'Integration-instance test ("Test" button) failed.\nBad status code: ' + str(response_code)
        prints_manager.add_print_job(test_failed_msg, print_error, thread_index)
        return (False, None)
    result_object = ast.literal_eval(response_data)
    success, failure_message = (bool(result_object.get('success')), result_object.get('message'))
    if not success:
        if failure_message:
            test_failed_msg = 'Test integration failed.\nFailure message: {}'.format(failure_message)
            prints_manager.add_print_job(test_failed_msg, print_error, thread_index)
        else:
            test_failed_msg = 'Test integration failed\nNo failure message.'
            prints_manager.add_print_job(test_failed_msg, print_error, thread_index)
    return (success, failure_message)