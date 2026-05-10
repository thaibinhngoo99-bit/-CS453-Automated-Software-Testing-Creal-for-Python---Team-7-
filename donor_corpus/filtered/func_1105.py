def is_port_open(port_or_url, http_path=None, expect_success=True, protocols=['tcp']):
    port = port_or_url
    host = 'localhost'
    protocol = 'http'
    protocols = protocols if isinstance(protocols, list) else [protocols]
    if isinstance(port, six.string_types):
        url = urlparse(port_or_url)
        port = url.port
        host = url.hostname
        protocol = url.scheme
    nw_protocols = []
    nw_protocols += [socket.SOCK_STREAM] if 'tcp' in protocols else []
    nw_protocols += [socket.SOCK_DGRAM] if 'udp' in protocols else []
    for nw_protocol in nw_protocols:
        with closing(socket.socket(socket.AF_INET, nw_protocol)) as sock:
            sock.settimeout(1)
            if nw_protocol == socket.SOCK_DGRAM:
                try:
                    if port == 53:
                        dnshost = '127.0.0.1' if host == 'localhost' else host
                        resolver = dns.resolver.Resolver()
                        resolver.nameservers = [dnshost]
                        resolver.timeout = 1
                        resolver.lifetime = 1
                        answers = resolver.query('google.com', 'A')
                        assert len(answers) > 0
                    else:
                        sock.sendto(bytes(), (host, port))
                        sock.recvfrom(1024)
                except Exception:
                    return False
            elif nw_protocol == socket.SOCK_STREAM:
                result = sock.connect_ex((host, port))
                if result != 0:
                    return False
    if 'tcp' not in protocols or not http_path:
        return True
    url = '%s://%s:%s%s' % (protocol, host, port, http_path)
    try:
        response = safe_requests.get(url)
        return not expect_success or response.status_code < 400
    except Exception:
        return False