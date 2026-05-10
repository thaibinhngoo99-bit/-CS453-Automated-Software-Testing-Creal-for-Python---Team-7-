def get_route(context, id):
    LOG.info('get_route %s for tenant %s' % (id, context.tenant_id))
    route = db_api.route_find(context, id=id, scope=db_api.ONE)
    if not route:
        raise quark_exceptions.RouteNotFound(route_id=id)
    return v._make_route_dict(route)