def tickers_nifty50(include_company_data=False, headers={'User-agent': 'Mozilla/5.0'}):
    """Downloads list of currently traded tickers on the NIFTY 50, India"""
    site = 'https://finance.yahoo.com/quote/%5ENSEI/components?p=%5ENSEI'
    table = pd.read_html(requests.get(site, headers=headers).text)[0]
    if include_company_data:
        return table
    nifty50 = sorted(table['Symbol'].tolist())
    return nifty50