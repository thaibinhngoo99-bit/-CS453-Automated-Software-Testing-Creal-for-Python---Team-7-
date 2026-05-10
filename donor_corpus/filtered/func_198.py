def tickers_ftse100(include_company_data=False):
    """Downloads a list of the tickers traded on the FTSE 100 index"""
    table = pd.read_html('https://en.wikipedia.org/wiki/FTSE_100_Index', attrs={'id': 'constituents'})[0]
    if include_company_data:
        return table
    return sorted(table.EPIC.tolist())