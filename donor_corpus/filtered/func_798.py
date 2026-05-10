def get_bucket_dynamic_path(path_list, b_map):
    if 'MAP' in b_map:
        map_dict = b_map['MAP']
    else:
        map_dict = b_map
    mapping = []
    log.debug('Pathparts is {0}'.format(', '.join(path_list)))
    for path_part in path_list:
        if mapping and isinstance(map_dict, str) or 'bucket' in map_dict:
            customheaders = {}
            if isinstance(map_dict, dict) and 'bucket' in map_dict:
                bucketname = map_dict['bucket']
                if 'headers' in map_dict:
                    customheaders = map_dict['headers']
            else:
                bucketname = map_dict
            log.debug(f'mapping: {mapping}')
            for _ in mapping:
                path_list.pop(0)
            object_name = '/'.join(path_list)
            bucket_path = '/'.join(mapping)
            log.info('Bucket mapping was {0}, object was {1}'.format(bucket_path, object_name))
            return (prepend_bucketname(bucketname), bucket_path, object_name, customheaders)
        if path_part in map_dict:
            map_dict = map_dict[path_part]
            mapping.append(path_part)
            log.debug('Found {0}, Mapping is now {1}'.format(path_part, '/'.join(mapping)))
        else:
            log.warning('Could not find {0} in bucketmap'.format(path_part))
            log.debug('said bucketmap: {}'.format(map_dict))
            return (False, False, False, {})
    return (False, False, False, {})