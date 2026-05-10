def get_routes(context):
    LOG.info('get_routes for tenant %s' % context.tenant_id)
    routes = db_api.route_find(context)
    return [v._make_route_dict(r) for r in routes]