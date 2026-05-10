def __delete_integrations_instances(client, module_instances, prints_manager, thread_index=0):
    succeed = True
    for module_instance in module_instances:
        succeed = __delete_integration_instance(client, module_instance['id'], thread_index=thread_index, prints_manager=prints_manager) and succeed
    return succeed