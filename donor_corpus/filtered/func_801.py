def bucket_prefix_match(bucket_check, bucket_map, object_name=''):
    log.debug(f"bucket_prefix_match(): checking if {bucket_check} matches {bucket_map} w/ optional obj '{object_name}'")
    if bucket_check == bucket_map.split('/')[0] and object_name.startswith('/'.join(bucket_map.split('/')[1:])):
        log.debug(f'Prefixed Bucket Map matched: s3://{bucket_check}/{object_name} => {bucket_map}')
        return True
    return False