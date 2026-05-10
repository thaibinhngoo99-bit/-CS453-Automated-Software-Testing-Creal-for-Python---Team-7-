def read_frame(websocket):
    header = Header.decode_header(websocket.stream)
    compressed = header.flags & header.RSV0_MASK
    if compressed:
        header.flags &= ~header.RSV0_MASK
    if header.flags:
        raise ProtocolError
    if not header.length:
        return (header, '')
    try:
        payload = websocket.raw_read(header.length)
    except error:
        payload = ''
    except Exception:
        raise WebSocketError('Could not read payload')
    if len(payload) != header.length:
        raise WebSocketError('Unexpected EOF reading frame payload')
    if header.mask:
        payload = header.unmask_payload(payload)
    if compressed:
        payload = ''.join((DECOMPRESSOR.decompress(payload), DECOMPRESSOR.decompress('\x00\x00ÿÿ'), DECOMPRESSOR.flush()))
    return (header, payload)