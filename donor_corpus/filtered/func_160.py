def balancer_absent(name, profile, **libcloud_kwargs):
    """
    Ensures a load balancer is absent.

    :param name: Load Balancer name
    :type  name: ``str``

    :param profile: The profile key
    :type  profile: ``str``
    """
    balancers = __salt__['libcloud_loadbalancer.list_balancers'](profile)
    match = [z for z in balancers if z['name'] == name]
    if len(match) == 0:
        return state_result(True, 'Balancer already absent', name)
    else:
        result = __salt__['libcloud_loadbalancer.destroy_balancer'](match[0]['id'], profile, **libcloud_kwargs)
        return state_result(result, 'Deleted load balancer', name)