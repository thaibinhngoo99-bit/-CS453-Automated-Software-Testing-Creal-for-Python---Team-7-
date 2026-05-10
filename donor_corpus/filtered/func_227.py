def get_premarket_price(ticker):
    """Inputs: @ticker
    
       Returns the current pre-market price of the input ticker
       (returns value if pre-market price is available."""
    quote_data = get_quote_data(ticker)
    if 'preMarketPrice' in quote_data:
        return quote_data['preMarketPrice']
    raise AssertionError('Premarket price not currently available.')