def build_list_request(subscription_id: str, resource_group_name: str, resource_name: str, **kwargs: Any) -> HttpRequest:
    api_version = kwargs.pop('api_version', '2022-04-01')
    accept = 'application/json'
    _url = kwargs.pop('template_url', '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/privateLinkResources')
    path_format_arguments = {'subscriptionId': _SERIALIZER.url('subscription_id', subscription_id, 'str', min_length=1), 'resourceGroupName': _SERIALIZER.url('resource_group_name', resource_group_name, 'str', max_length=90, min_length=1), 'resourceName': _SERIALIZER.url('resource_name', resource_name, 'str', max_length=63, min_length=1, pattern='^[a-zA-Z0-9]$|^[a-zA-Z0-9][-_a-zA-Z0-9]{0,61}[a-zA-Z0-9]$')}
    _url = _format_url_section(_url, **path_format_arguments)
    _query_parameters = kwargs.pop('params', {})
    _query_parameters['api-version'] = _SERIALIZER.query('api_version', api_version, 'str')
    _header_parameters = kwargs.pop('headers', {})
    _header_parameters['Accept'] = _SERIALIZER.header('accept', accept, 'str')
    return HttpRequest(method='GET', url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)