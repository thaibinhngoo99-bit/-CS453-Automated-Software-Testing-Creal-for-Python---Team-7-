def make_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((config['host'], config['port']))
    sock.listen(5)
    return sock