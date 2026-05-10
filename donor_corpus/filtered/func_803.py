def check_private_bucket(bucket, b_map, object_name=''):
    log.debug('check_private_buckets(): bucket: {}'.format(bucket))
    if 'PRIVATE_BUCKETS' in b_map:
        sorted_buckets = get_sorted_bucket_list(b_map, 'PRIVATE_BUCKETS')
        log.debug(f'Sorted PRIVATE buckets are {sorted_buckets}')
        for priv_bucket in sorted_buckets:
            if bucket_prefix_match(bucket, prepend_bucketname(priv_bucket), object_name):
                return b_map['PRIVATE_BUCKETS'][priv_bucket]
    return False