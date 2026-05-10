def http_file_exists(url):
    exists = False
    try:
        conn = http.HTTPConnection(url.netloc)
        conn.request('HEAD', url.path)
        response = conn.getresponse()
        exists = response.status == 200
    except:
        pass
    return exists