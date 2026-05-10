def balancer_present(name, port, protocol, profile, algorithm=None, members=None, **libcloud_kwargs):
    """
    Ensures a load balancer is present.

    :param name: Load Balancer name
    :type  name: ``str``

    :param port: Port the load balancer should listen on, defaults to 80
    :type  port: ``str``

    :param protocol: Loadbalancer protocol, defaults to http.
    :type  protocol: ``str``

    :param profile: The profile key
    :type  profile: ``str``

    :param algorithm: Load balancing algorithm, defaults to ROUND_ROBIN. See Algorithm type
        in Libcloud documentation for a full listing.
    :type algorithm: ``str``

    :param members: An optional list of members to create on deployment
    :type  members: ``list`` of ``dict`` (ip, port)
    """
    balancers = __salt__['libcloud_loadbalancer.list_balancers'](profile)
    match = [z for z in balancers if z['name'] == name]
    if len(match) > 0:
        return state_result(True, 'Balancer already exists', name)
    else:
        starting_members = None
        if members is not None:
            starting_members = []
            for m in members:
                starting_members.append({'ip': m['ip'], 'port': m['port']})
        balancer = __salt__['libcloud_loadbalancer.create_balancer'](name, port, protocol, profile, algorithm=algorithm, members=starting_members, **libcloud_kwargs)
        return state_result(True, 'Created new load balancer', name, balancer)