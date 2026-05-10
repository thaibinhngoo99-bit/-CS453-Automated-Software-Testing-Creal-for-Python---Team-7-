def dump_hash(twitter_dump):
    data_hash = None
    dump = hashlib.sha1()
    dump.update(twitter_dump)
    data_hash = dump.hexdigest()
    return data_hash