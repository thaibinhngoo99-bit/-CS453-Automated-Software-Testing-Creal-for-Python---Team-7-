def serve(host, port):
    global listener
    listener = sockets.serve('Client', Client, host, port)
    return listener.getsockname()