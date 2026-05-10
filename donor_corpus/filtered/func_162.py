def member_absent(ip, port, balancer_id, profile, **libcloud_kwargs):
    """
    Ensure a load balancer member is absent, based on IP and Port

    :param ip: IP address for the member
    :type  ip: ``str``

    :param port: Port for the member
    :type  port: ``int``

    :param balancer_id: id of a load balancer you want to detach the member from
    :type  balancer_id: ``str``

    :param profile: The profile key
    :type  profile: ``str``
    """
    existing_members = __salt__['libcloud_loadbalancer.list_balancer_members'](balancer_id, profile)
    for member in existing_members:
        if member['ip'] == ip and member['port'] == port:
            result = __salt__['libcloud_loadbalancer.balancer_detach_member'](balancer_id, member['id'], profile, **libcloud_kwargs)
            return state_result(result, 'Member removed', balancer_id)
    return state_result(True, 'Member already absent', balancer_id)