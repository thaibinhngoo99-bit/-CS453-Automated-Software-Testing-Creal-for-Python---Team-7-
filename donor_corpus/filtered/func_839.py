def create_route(context, route):
    LOG.info('create_route for tenant %s' % context.tenant_id)
    route = route['route']
    for key in ['gateway', 'cidr', 'subnet_id']:
        if key not in route:
            raise exceptions.BadRequest(resource='routes', msg='%s is required' % key)
    subnet_id = route['subnet_id']
    with context.session.begin():
        subnet = db_api.subnet_find(context, id=subnet_id, scope=db_api.ONE)
        if not subnet:
            raise exceptions.SubnetNotFound(subnet_id=subnet_id)
        policies = db_models.IPPolicy.get_ip_policy_cidrs(subnet)
        alloc_pools = allocation_pool.AllocationPools(subnet['cidr'], policies=policies)
        alloc_pools.validate_gateway_excluded(route['gateway'])
        route_cidr = netaddr.IPNetwork(route['cidr'])
        subnet_routes = db_api.route_find(context, subnet_id=subnet_id, scope=db_api.ALL)
        quota.QUOTAS.limit_check(context, context.tenant_id, routes_per_subnet=len(subnet_routes) + 1)
        for sub_route in subnet_routes:
            sub_route_cidr = netaddr.IPNetwork(sub_route['cidr'])
            if sub_route_cidr.value == DEFAULT_ROUTE.value:
                continue
            if route_cidr in sub_route_cidr or sub_route_cidr in route_cidr:
                raise quark_exceptions.RouteConflict(route_id=sub_route['id'], cidr=str(route_cidr))
        new_route = db_api.route_create(context, **route)
    return v._make_route_dict(new_route)