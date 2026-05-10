def run(cmd, cache_duration_secs=0, **kwargs):

    def do_run(cmd):
        return bootstrap.run(cmd, **kwargs)
    if cache_duration_secs <= 0:
        return do_run(cmd)
    hash = md5(cmd)
    cache_file = CACHE_FILE_PATTERN.replace('*', hash)
    mkdir(os.path.dirname(CACHE_FILE_PATTERN))
    if os.path.isfile(cache_file):
        mod_time = os.path.getmtime(cache_file)
        time_now = now()
        if mod_time > time_now - cache_duration_secs:
            f = open(cache_file)
            result = f.read()
            f.close()
            return result
    result = do_run(cmd)
    f = open(cache_file, 'w+')
    f.write(result)
    f.close()
    clean_cache()
    return result