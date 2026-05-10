def download(download_link, output_folder, package_name, version):
    url = download_link
    dst = Path(output_folder).joinpath('{}_{}.tar.gz'.format(package_name, version))
    urlretrieve(url, dst)