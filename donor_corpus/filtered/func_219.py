def get_earnings_history(ticker):
    """Inputs: @ticker
           Returns the earnings calendar history of the input ticker with 
           EPS actual vs. expected data."""
    url = 'https://finance.yahoo.com/calendar/earnings?symbol=' + ticker
    result = _parse_earnings_json(url)
    return result['context']['dispatcher']['stores']['ScreenerResultsStore']['results']['rows']