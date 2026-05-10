def parse_chunked_data(data):
    """ Parse the body of an HTTP message transmitted with chunked transfer encoding. """
    data = (data or '').strip()
    chunks = []
    while data:
        length = re.match('^([0-9a-zA-Z]+)\\r\\n.*', data)
        if not length:
            break
        length = length.group(1).lower()
        length = int(length, 16)
        data = data.partition('\r\n')[2]
        chunks.append(data[:length])
        data = data[length:].strip()
    return ''.join(chunks)