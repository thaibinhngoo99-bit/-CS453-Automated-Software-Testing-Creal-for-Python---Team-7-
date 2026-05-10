def get_stats(ticker, headers={'User-agent': 'Mozilla/5.0'}):
    """Scrapes information from the statistics tab on Yahoo Finance 
       for an input ticker 
    
       @param: ticker
    """
    stats_site = 'https://finance.yahoo.com/quote/' + ticker + '/key-statistics?p=' + ticker
    tables = pd.read_html(requests.get(stats_site, headers=headers).text)
    tables = [table for table in tables[1:] if table.shape[1] == 2]
    table = tables[0]
    for elt in tables[1:]:
        table = table.append(elt)
    table.columns = ['Attribute', 'Value']
    table = table.reset_index(drop=True)
    return table