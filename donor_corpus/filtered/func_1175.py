def extract_all_api_info_for_service(service, path_prefix):
    """Return a dictionary mapping each API method to a list of tuples [(path, HTTP method)]"""
    service_methods = service.DESCRIPTOR.methods
    res = {}
    for service_method in service_methods:
        endpoints = service_method.GetOptions().Extensions[databricks_pb2.rpc].endpoints
        res[service().GetRequestClass(service_method)] = [(_get_path(path_prefix, endpoint.path), endpoint.method) for endpoint in endpoints]
    return res