def __create_incident_with_playbook(client, name, playbook_id, integrations, prints_manager, thread_index=0):
    create_incident_request = demisto_client.demisto_api.CreateIncidentRequest()
    create_incident_request.create_investigation = True
    create_incident_request.playbook_id = playbook_id
    create_incident_request.name = name
    try:
        response = client.create_incident(create_incident_request=create_incident_request)
    except ApiException as err:
        prints_manager.add_print_job(str(err), print_error, thread_index)
    try:
        inc_id = response.id
    except:
        inc_id = 'incCreateErr'
    if inc_id == 'incCreateErr':
        integration_names = [integration['name'] for integration in integrations if 'name' in integration]
        error_message = 'Failed to create incident for integration names: {} and playbookID: {}.Possible reasons are:\nMismatch between playbookID in conf.json and the id of the real playbook you were trying to use,or schema problems in the TestPlaybook.'.format(str(integration_names), playbook_id)
        prints_manager.add_print_job(error_message, print_error, thread_index)
        return (False, -1)
    search_filter = demisto_client.demisto_api.SearchIncidentsData()
    inc_filter = demisto_client.demisto_api.IncidentFilter()
    inc_filter.query = 'id:' + str(inc_id)
    search_filter.filter = inc_filter
    try:
        incidents = client.search_incidents(filter=search_filter)
    except ApiException as err:
        prints_manager.add_print_job(err, print, thread_index)
        incidents = {'total': 0}
    timeout = time.time() + 120
    while incidents['total'] != 1:
        try:
            incidents = client.search_incidents(filter=search_filter)
        except ApiException as err:
            prints_manager.add_print_job(err, print, thread_index)
        if time.time() > timeout:
            error_message = 'Got timeout for searching incident with id {}, got {} incidents in the search'.format(inc_id, incidents['total'])
            prints_manager.add_print_job(error_message, print_error, thread_index)
            return (False, -1)
        time.sleep(1)
    return (incidents['data'][0], inc_id)