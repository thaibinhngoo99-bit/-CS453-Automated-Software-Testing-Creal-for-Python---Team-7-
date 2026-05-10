def absent(name, region=None, key=None, keyid=None, profile=None):
    """
    Delete the kinesis stream, if it exists.

    name (string)
        Stream name

    region (string)
        Region to connect to.

    key (string)
        Secret key to be used.

    keyid (string)
        Access key to be used.

    profile (dict)
        A dict with region, key and keyid, or a pillar key (string)
        that contains a dict with region, key and keyid.
    """
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    exists = __salt__['boto_kinesis.exists'](name, region, key, keyid, profile)
    if exists['result'] is False:
        ret['comment'] = 'Kinesis stream {0} does not exist'.format(name)
        return ret
    if __opts__['test']:
        ret['comment'] = 'Kinesis stream {0} would be deleted'.format(name)
        ret['result'] = None
        return ret
    is_deleted = __salt__['boto_kinesis.delete_stream'](name, region, key, keyid, profile)
    if 'error' in is_deleted:
        ret['comment'] = 'Failed to delete stream {0}: {1}'.format(name, is_deleted['error'])
        ret['result'] = False
    else:
        ret['comment'] = 'Deleted stream {0}'.format(name)
        ret['changes'].setdefault('old', 'Stream {0} exists'.format(name))
        ret['changes'].setdefault('new', 'Stream {0} deleted'.format(name))
    return ret