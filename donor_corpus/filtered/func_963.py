@app.route('/streams/<int:server>/<path:path>')
def get_stream_file(server, path):
    full_url = 'http://edge{}.stream.highwebmedia.com:1935/{}'.format(server, path)
    resp = requests.get(full_url, stream=True)
    content = resp.iter_content(chunk_size=2 ** 16)
    status_code = resp.status_code
    content_type = resp.headers.get('content-type', 'application/octet-stream')
    return flask.Response(content, status=status_code, mimetype=content_type)