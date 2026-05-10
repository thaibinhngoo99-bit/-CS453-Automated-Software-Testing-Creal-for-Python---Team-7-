def check_public_bucket(bucket, b_map, object_name=''):
    if 'PUBLIC_BUCKETS' in b_map:
        sorted_buckets = get_sorted_bucket_list(b_map, 'PUBLIC_BUCKETS')
        log.debug(f'Sorted PUBLIC buckets are {sorted_buckets}')
        for pub_bucket in sorted_buckets:
            if bucket_prefix_match(bucket, prepend_bucketname(pub_bucket), object_name):
                log.debug("found a public, we'll take it")
                return True
    log.debug('we did not find a public bucket for {}'.format(bucket))
    return False