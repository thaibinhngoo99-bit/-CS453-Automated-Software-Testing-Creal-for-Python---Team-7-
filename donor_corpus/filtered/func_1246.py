def get_metadata(name):
    encoded_name = str(base64.urlsafe_b64encode(name.encode('utf-8')), 'utf-8')
    b = base.get(encoded_name)
    if b:
        return b
    return None