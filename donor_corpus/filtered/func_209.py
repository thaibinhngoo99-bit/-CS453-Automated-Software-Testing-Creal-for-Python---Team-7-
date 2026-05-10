def get_holders(ticker, headers={'User-agent': 'Mozilla/5.0'}):
    """Scrapes the Holders page from Yahoo Finance for an input ticker 
    
       @param: ticker
    """
    holders_site = 'https://finance.yahoo.com/quote/' + ticker + '/holders?p=' + ticker
    tables = pd.read_html(requests.get(holders_site, headers=headers).text)
    table_names = ['Major Holders', 'Direct Holders (Forms 3 and 4)', 'Top Institutional Holders', 'Top Mutual Fund Holders']
    table_mapper = {key: val for key, val in zip(table_names, tables)}
    return table_mapper