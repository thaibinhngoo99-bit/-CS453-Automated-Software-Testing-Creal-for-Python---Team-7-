def get_postmarket_price(ticker):
    """Inputs: @ticker
    
       Returns the current post-market price of the input ticker
       (returns value if pre-market price is available."""
    quote_data = get_quote_data(ticker)
    if 'postMarketPrice' in quote_data:
        return quote_data['postMarketPrice']
    raise AssertionError('Postmarket price not currently available.')