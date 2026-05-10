import socket
import time

from xmlrpclib_to import ServerProxy
import httpretty
import pytest


XML_RESPONSE = """<?xml version="1.0"?>
<methodResponse>
    <params>
        <param>
            <value><string>Test</string></value>
        </param>
    </params>
</methodResponse>"""


def timeout(request, url, headers):
        time.sleep(1)
        return 200, headers, XML_RESPONSE


@httpretty.activate
def test_timeout():

    httpretty.register_uri(
        httpretty.POST,
        'http://example.com/RPC2',
        content_type='text/xml',
        body=timeout
    )
    proxy = ServerProxy('http://example.com', timeout=0.5)
    with pytest.raises(socket.timeout):
        proxy.test()


@httpretty.activate
def test_timeout_https():
    httpretty.register_uri(
        httpretty.POST,
        'https://example.com/RPC2',
        content_type='text/xml',
        body=timeout
    )

    proxy = ServerProxy('https://example.com', timeout=0.5)
    with pytest.raises(socket.timeout):
        proxy.test()


if __name__ == "__main__":
    test_timeout()
    test_timeout_https()

