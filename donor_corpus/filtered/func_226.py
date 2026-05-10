def get_market_status():
    """Returns the current state of the market - PRE, POST, OPEN, or CLOSED"""
    quote_data = get_quote_data('^dji')
    return quote_data['marketState']