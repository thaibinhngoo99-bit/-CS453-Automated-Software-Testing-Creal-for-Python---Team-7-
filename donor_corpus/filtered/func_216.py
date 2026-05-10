def get_earnings(ticker):
    """Scrapes earnings data from Yahoo Finance for an input ticker 
    
       @param: ticker
    """
    result = {'quarterly_results': pd.DataFrame(), 'yearly_revenue_earnings': pd.DataFrame(), 'quarterly_revenue_earnings': pd.DataFrame()}
    financials_site = 'https://finance.yahoo.com/quote/' + ticker + '/financials?p=' + ticker
    json_info = _parse_json(financials_site)
    if 'earnings' not in json_info:
        return result
    temp = json_info['earnings']
    if temp == None:
        return result
    result['quarterly_results'] = pd.DataFrame.from_dict(temp['earningsChart']['quarterly'])
    result['yearly_revenue_earnings'] = pd.DataFrame.from_dict(temp['financialsChart']['yearly'])
    result['quarterly_revenue_earnings'] = pd.DataFrame.from_dict(temp['financialsChart']['quarterly'])
    return result