def _encode_bytes(text):
    if isinstance(text, str):
        return text
    if not isinstance(text, unicode):
        text = unicode(text or '')
    return text.encode('utf-8')