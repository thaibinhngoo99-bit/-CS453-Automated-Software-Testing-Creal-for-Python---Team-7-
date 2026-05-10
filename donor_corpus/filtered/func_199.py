def tickers_ftse250(include_company_data=False):
    """Downloads a list of the tickers traded on the FTSE 250 index"""
    table = pd.read_html('https://en.wikipedia.org/wiki/FTSE_250_Index', attrs={'id': 'constituents'})[0]
    table.columns = ['Company', 'Ticker']
    if include_company_data:
        return table
    return sorted(table.Ticker.tolist())