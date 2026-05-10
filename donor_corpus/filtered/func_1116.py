def download(url, path, verify_ssl=True):
    """Downloads file at url to the given path"""
    s = requests.Session()
    r = s.get(url, stream=True, verify=verify_ssl)
    if r.status_code >= 400:
        raise Exception('Failed to download %s, response code %s' % (url, r.status_code))
    total = 0
    try:
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        LOG.debug('Starting download from %s to %s (%s bytes)' % (url, path, r.headers.get('content-length')))
        with open(path, 'wb') as f:
            for chunk in r.iter_content(DOWNLOAD_CHUNK_SIZE):
                total += len(chunk)
                if chunk:
                    f.write(chunk)
                    LOG.debug('Writing %s bytes (total %s) to %s' % (len(chunk), total, path))
                else:
                    LOG.debug('Empty chunk %s (total %s) from %s' % (chunk, total, url))
            f.flush()
            os.fsync(f)
        if os.path.getsize(path) == 0:
            LOG.warning('Zero bytes downloaded from %s, retrying' % url)
            download(url, path, verify_ssl)
            return
        LOG.debug('Done downloading %s, response code %s, total bytes %d' % (url, r.status_code, total))
    finally:
        LOG.debug('Cleaning up file handles for download of %s' % url)
        r.close()
        s.close()