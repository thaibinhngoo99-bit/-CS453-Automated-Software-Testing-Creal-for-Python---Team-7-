def clean_cache(file_pattern=CACHE_FILE_PATTERN, last_clean_time=last_cache_clean_time, max_age=CACHE_MAX_AGE):
    mutex_clean.acquire()
    time_now = now()
    try:
        if last_clean_time['time'] > time_now - CACHE_CLEAN_TIMEOUT:
            return
        for cache_file in set(glob.glob(file_pattern)):
            mod_time = os.path.getmtime(cache_file)
            if time_now > mod_time + max_age:
                rm_rf(cache_file)
        last_clean_time['time'] = time_now
    finally:
        mutex_clean.release()
    return time_now