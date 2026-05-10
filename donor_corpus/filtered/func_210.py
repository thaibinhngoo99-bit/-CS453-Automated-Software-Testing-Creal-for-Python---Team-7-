def get_analysts_info(ticker, headers={'User-agent': 'Mozilla/5.0'}):
    """Scrapes the Analysts page from Yahoo Finance for an input ticker 
    
       @param: ticker
    """
    analysts_site = 'https://finance.yahoo.com/quote/' + ticker + '/analysts?p=' + ticker
    tables = pd.read_html(requests.get(analysts_site, headers=headers).text)
    table_names = [table.columns[0] for table in tables]
    table_mapper = {key: val for key, val in zip(table_names, tables)}
    return table_mapper