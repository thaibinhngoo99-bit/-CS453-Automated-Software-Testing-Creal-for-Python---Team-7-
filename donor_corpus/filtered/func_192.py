def tickers_nasdaq(include_company_data=False):
    """Downloads list of tickers currently listed in the NASDAQ"""
    ftp = ftplib.FTP('ftp.nasdaqtrader.com')
    ftp.login()
    ftp.cwd('SymbolDirectory')
    r = io.BytesIO()
    ftp.retrbinary('RETR nasdaqlisted.txt', r.write)
    if include_company_data:
        r.seek(0)
        data = pd.read_csv(r, sep='|')
        return data
    info = r.getvalue().decode()
    splits = info.split('|')
    tickers = [x for x in splits if '\r\n' in x]
    tickers = [x.split('\r\n')[1] for x in tickers if 'NASDAQ' not in x != '\r\n']
    tickers = [ticker for ticker in tickers if 'File' not in ticker]
    ftp.close()
    return tickers