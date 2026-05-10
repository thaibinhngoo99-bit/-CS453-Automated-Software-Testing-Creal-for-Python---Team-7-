def make_compressed_frame(message, compressor):
    """
    Make a compressed websocket frame from a message and compressor.

    Generates header and a compressed message which can then be used on any
    websocket connection where `no_context_takeover` has been negotiated.
    This prevents the need to re-compress a broadcast-style message for every
    websocket connection.

    `compressor` is a zlib compressor object.
    """
    binary = not isinstance(message, (str, unicode))
    opcode = WebSocket.OPCODE_BINARY if binary else WebSocket.OPCODE_TEXT
    if binary:
        message = str(message)
    else:
        message = _encode_bytes(message)
    message = compressor.compress(message)
    message += compressor.flush(Z_FULL_FLUSH)
    if message.endswith('\x00\x00ÿÿ'):
        message = message[:-4]
    flags = Header.RSV0_MASK
    header = Header.encode_header(fin=True, opcode=opcode, mask='', length=len(message), flags=flags)
    return header + message