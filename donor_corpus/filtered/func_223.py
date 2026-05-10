def get_futures(headers={'User-agent': 'Mozilla/5.0'}):
    """Returns the futures table from Yahoo Finance"""
    site = 'https://finance.yahoo.com/commodities'
    tables = pd.read_html(requests.get(site, headers=headers).text)
    result = tables[0]
    return result