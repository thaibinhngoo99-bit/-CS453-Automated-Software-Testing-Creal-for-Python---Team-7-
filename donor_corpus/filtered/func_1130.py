def remove_non_ascii(text):
    text = text.decode('utf-8', CODEC_HANDLER_UNDERSCORE)
    text = text.encode('ascii', CODEC_HANDLER_UNDERSCORE)
    return text