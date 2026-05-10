def get_currencies(headers={'User-agent': 'Mozilla/5.0'}):
    """Returns the currencies table from Yahoo Finance"""
    site = 'https://finance.yahoo.com/currencies'
    tables = pd.read_html(requests.get(site, headers=headers).text)
    result = tables[0]
    return result