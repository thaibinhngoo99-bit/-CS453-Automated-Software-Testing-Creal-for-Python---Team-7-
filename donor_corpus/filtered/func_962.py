def get_user_stream(user):
    page = requests.get('https://chaturbate.com/{}/?use_html_chat=1'.format(user)).text
    match = re.search('<video .*src="(.+?)"', page)
    if not match:
        return ''
    playlist = match.group(1).replace(' ', '%20')
    playlist = urllib.parse.urlparse(playlist)
    server_number = re.sub('[^\\d]', '', playlist.netloc.split('.')[0])
    return '/streams/{}{}'.format(server_number, playlist.path)