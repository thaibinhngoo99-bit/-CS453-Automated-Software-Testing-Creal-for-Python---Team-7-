def tickers_dow(include_company_data=False):
    """Downloads list of currently traded tickers on the Dow"""
    site = 'https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average'
    table = pd.read_html(site, attrs={'id': 'constituents'})[0]
    if include_company_data:
        return table
    dow_tickers = sorted(table['Symbol'].tolist())
    return dow_tickers