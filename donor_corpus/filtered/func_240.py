def get_service_endpoint(service, region):
    loader = botocore.loaders.create_loader()
    data = loader.load_data('endpoints')
    resolver = botocore.regions.EndpointResolver(data)
    endpoint_data = resolver.construct_endpoint(service, region)
    return 'https://' + endpoint_data['hostname']