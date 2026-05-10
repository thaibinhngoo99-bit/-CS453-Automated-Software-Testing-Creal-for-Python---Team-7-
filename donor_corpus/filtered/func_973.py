def ftp_file_exists(url):
    listing = []
    try:
        conn = ftplib.FTP(url.netloc)
        conn.login()
        listing = conn.nlst(url.path)
        conn.quit()
    except Exception as e:
        pass
    return len(listing) > 0