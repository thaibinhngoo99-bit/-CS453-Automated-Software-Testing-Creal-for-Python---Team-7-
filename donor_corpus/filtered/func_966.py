def start_wsgi_server():
    sock = make_socket()
    server = gevent.pywsgi.WSGIServer(sock, app)
    server.serve_forever()