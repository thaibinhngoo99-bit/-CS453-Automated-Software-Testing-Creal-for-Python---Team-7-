def get_stats_valuation(ticker, headers={'User-agent': 'Mozilla/5.0'}):
    """Scrapes Valuation Measures table from the statistics tab on Yahoo Finance 
       for an input ticker 
    
       @param: ticker
    """
    stats_site = 'https://finance.yahoo.com/quote/' + ticker + '/key-statistics?p=' + ticker
    tables = pd.read_html(requests.get(stats_site, headers=headers).text)
    tables = [table for table in tables if 'Trailing P/E' in table.iloc[:, 0].tolist()]
    table = tables[0].reset_index(drop=True)
    return table