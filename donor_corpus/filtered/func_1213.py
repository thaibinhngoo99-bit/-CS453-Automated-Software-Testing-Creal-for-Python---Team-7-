def nicovideo_download(url, output_dir='.', merge=True, info_only=False):
    import ssl
    ssl_context = request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))
    cookie_handler = request.HTTPCookieProcessor()
    opener = request.build_opener(ssl_context, cookie_handler)
    request.install_opener(opener)
    import netrc, getpass
    try:
        info = netrc.netrc().authenticators('nicovideo')
    except FileNotFoundError:
        info = None
    if info is None:
        user = input('User:     ')
        password = getpass.getpass('Password: ')
    else:
        user, password = (info[0], info[2])
    print('Logging in...')
    nicovideo_login(user, password)
    html = get_html(url)
    title = unicodize(r1('<span class="videoHeaderTitle"[^>]*>([^<]+)</span>', html))
    vid = url.split('/')[-1].split('?')[0]
    api_html = get_html('http://www.nicovideo.jp/api/getflv?v=%s' % vid)
    real_url = parse.unquote(r1('url=([^&]+)&', api_html))
    type, ext, size = url_info(real_url)
    print_info(site_info, title, type, size)
    if not info_only:
        download_urls([real_url], title, ext, size, output_dir, merge=merge)