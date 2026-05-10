def get_cash_flow(ticker, yearly=True):
    """Scrapes the cash flow statement from Yahoo Finance for an input ticker 
    
       @param: ticker
    """
    cash_flow_site = 'https://finance.yahoo.com/quote/' + ticker + '/cash-flow?p=' + ticker
    json_info = _parse_json(cash_flow_site)
    if yearly:
        temp = json_info['cashflowStatementHistory']['cashflowStatements']
    else:
        temp = json_info['cashflowStatementHistoryQuarterly']['cashflowStatements']
    return _parse_table(temp)