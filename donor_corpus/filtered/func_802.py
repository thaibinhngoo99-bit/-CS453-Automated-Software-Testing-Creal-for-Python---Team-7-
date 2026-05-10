def get_sorted_bucket_list(b_map, bucket_group):
    if bucket_group not in b_map:
        log.warning(f"Bucket map does not contain bucket group '{bucket_group}'")
        return []
    if isinstance(b_map[bucket_group], dict):
        return sorted(list(b_map[bucket_group].keys()), key=lambda e: e.count('/'), reverse=True)
    if isinstance(b_map[bucket_group], list):
        return sorted(list(b_map[bucket_group]), key=lambda e: e.count('/'), reverse=True)
    return []