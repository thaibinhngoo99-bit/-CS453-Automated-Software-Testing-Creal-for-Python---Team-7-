def get_income_statement(ticker, yearly=True):
    """Scrape income statement from Yahoo Finance for a given ticker
    
       @param: ticker
    """
    income_site = 'https://finance.yahoo.com/quote/' + ticker + '/financials?p=' + ticker
    json_info = _parse_json(income_site)
    if yearly:
        temp = json_info['incomeStatementHistory']['incomeStatementHistory']
    else:
        temp = json_info['incomeStatementHistoryQuarterly']['incomeStatementHistory']
    return _parse_table(temp)