def file_hash(point_to_file):
    hash_sha1 = hashlib.sha1()
    with open(point_to_file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_sha1.update(chunk)
    print(hash_sha1.hexdigest())
    return hash_sha1.hexdigest()