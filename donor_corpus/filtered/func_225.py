def get_quote_data(ticker, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}):
    """Inputs: @ticker
    
       Returns a dictionary containing over 70 elements corresponding to the 
       input ticker, including company name, book value, moving average data,
       pre-market / post-market price (when applicable), and more."""
    site = 'https://query1.finance.yahoo.com/v7/finance/quote?symbols=' + ticker
    resp = requests.get(site, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    if not resp.ok:
        raise AssertionError('Invalid response from server.  Check if ticker is\n                              valid.')
    json_result = resp.json()
    info = json_result['quoteResponse']['result']
    return info[0]