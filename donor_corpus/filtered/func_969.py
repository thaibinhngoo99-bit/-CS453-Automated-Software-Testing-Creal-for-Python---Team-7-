def make_inventory(inventory_filename, deploy_dir=None, ssh_port=None, ssh_user=None, ssh_key=None, ssh_key_password=None, ssh_password=None, winrm_username=None, winrm_password=None, winrm_port=None):
    """
    Builds a ``pyinfra.api.Inventory`` from the filesystem. If the file does not exist
    and doesn't contain a / attempts to use that as the only hostname.
    """
    if ssh_port is not None:
        ssh_port = int(ssh_port)
    file_groupname = None
    if not path.exists(inventory_filename):
        groups = {'all': inventory_filename.split(',')}
    else:
        groups = _get_groups_from_filename(inventory_filename)
        file_groupname = path.basename(inventory_filename).rsplit('.')[0]
    all_data = {}
    if 'all' in groups:
        all_hosts = groups.pop('all')
        if isinstance(all_hosts, tuple):
            all_hosts, all_data = all_hosts
    else:
        all_hosts = []
        for hosts in groups.values():
            hosts = hosts[0] if isinstance(hosts, tuple) else hosts
            for host in hosts:
                hostname = host[0] if isinstance(host, tuple) else host
                if hostname not in all_hosts:
                    all_hosts.append(hostname)
    groups['all'] = (all_hosts, all_data)
    if file_groupname and file_groupname not in groups:
        groups[file_groupname] = all_hosts
    logger.debug('Creating fake inventory...')
    fake_groups = {name: group if isinstance(group, tuple) else (group, {}) for name, group in six.iteritems(groups)}
    fake_inventory = Inventory((all_hosts, all_data), **fake_groups)
    pseudo_inventory.set(fake_inventory)
    group_data = _get_group_data(deploy_dir)
    pseudo_inventory.reset()
    for name, hosts in six.iteritems(groups):
        data = {}
        if isinstance(hosts, tuple):
            hosts, data = hosts
        if name in group_data:
            data.update(group_data.pop(name))
        groups[name] = (hosts, data)
    for name, data in six.iteritems(group_data):
        groups[name] = ([], data)
    return (Inventory(groups.pop('all'), ssh_user=ssh_user, ssh_key=ssh_key, ssh_key_password=ssh_key_password, ssh_port=ssh_port, ssh_password=ssh_password, winrm_username=winrm_username, winrm_password=winrm_password, winrm_port=winrm_port, **groups), file_groupname and file_groupname.lower())