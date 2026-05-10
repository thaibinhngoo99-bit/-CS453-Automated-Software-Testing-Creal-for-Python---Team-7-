def get_undervalued_large_caps(headers={'User-agent': 'Mozilla/5.0'}):
    """Returns the undervalued large caps table from Yahoo Finance"""
    site = 'https://finance.yahoo.com/screener/predefined/undervalued_large_caps?offset=0&count=100'
    tables = pd.read_html(requests.get(site, headers=headers).text)
    result = tables[0]
    return result