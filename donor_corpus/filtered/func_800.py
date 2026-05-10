def process_request(varargs, b_map):
    varargs = varargs.split('/')
    if len(varargs) < 2:
        return ('/'.join(varargs), None, None, [])
    if len(varargs) == 3:
        if os.getenv('USE_REVERSE_BUCKET_MAP', 'FALSE').lower() == 'true':
            varargs[0], varargs[1] = (varargs[1], varargs[0])
    bucket, path, object_name, headers = get_bucket_dynamic_path(varargs, b_map)
    if not bucket:
        object_name = varargs.pop(-1)
        path = '/'.join(varargs)
    return (path, bucket, object_name, headers)