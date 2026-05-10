def md5(string):
    m = hashlib.md5()
    m.update(to_bytes(string))
    return m.hexdigest()