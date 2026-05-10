def get_balance_sheet(ticker, yearly=True):
    """Scrapes balance sheet from Yahoo Finance for an input ticker 
    
       @param: ticker
    """
    balance_sheet_site = 'https://finance.yahoo.com/quote/' + ticker + '/balance-sheet?p=' + ticker
    json_info = _parse_json(balance_sheet_site)
    try:
        if yearly:
            temp = json_info['balanceSheetHistory']['balanceSheetStatements']
        else:
            temp = json_info['balanceSheetHistoryQuarterly']['balanceSheetStatements']
    except:
        temp = []
    return _parse_table(temp)