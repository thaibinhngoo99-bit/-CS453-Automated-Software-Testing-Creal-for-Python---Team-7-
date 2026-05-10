def get_financials(ticker, yearly=True, quarterly=True):
    """Scrapes financials data from Yahoo Finance for an input ticker, including
       balance sheet, cash flow statement, and income statement.  Returns dictionary
       of results.
    
       @param: ticker
       @param: yearly = True
       @param: quarterly = True
    """
    if not yearly and (not quarterly):
        raise AssertionError('yearly or quarterly must be True')
    financials_site = 'https://finance.yahoo.com/quote/' + ticker + '/financials?p=' + ticker
    json_info = _parse_json(financials_site)
    result = {}
    if yearly:
        temp = json_info['incomeStatementHistory']['incomeStatementHistory']
        table = _parse_table(temp)
        result['yearly_income_statement'] = table
        temp = json_info['balanceSheetHistory']['balanceSheetStatements']
        table = _parse_table(temp)
        result['yearly_balance_sheet'] = table
        temp = json_info['cashflowStatementHistory']['cashflowStatements']
        table = _parse_table(temp)
        result['yearly_cash_flow'] = table
    if quarterly:
        temp = json_info['incomeStatementHistoryQuarterly']['incomeStatementHistory']
        table = _parse_table(temp)
        result['quarterly_income_statement'] = table
        temp = json_info['balanceSheetHistoryQuarterly']['balanceSheetStatements']
        table = _parse_table(temp)
        result['quarterly_balance_sheet'] = table
        temp = json_info['cashflowStatementHistoryQuarterly']['cashflowStatements']
        table = _parse_table(temp)
        result['quarterly_cash_flow'] = table
    return result