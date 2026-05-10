def get_packages(package_name):
    """
    Note that package name already starts with /simple/
    This downloader only focuses on .tar.gz files

    :param package_name:
    :return:
    """
    url = 'https://pypi.org{}'.format(package_name)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='html.parser')
    tar = 0
    for id, link in enumerate(soup.find_all('a', href=True)):
        if '.tar.gz' in link['href']:
            download(link['href'], 'downloaded_packages/tar', package_name.split('/')[-2], id)
            tar += 1
    return {'tar': tar}