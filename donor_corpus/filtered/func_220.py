def get_earnings_for_date(date, offset=0, count=1):
    """Inputs: @date
       Returns a dictionary of stock tickers with earnings expected on the
       input date.  The dictionary contains the expected EPS values for each
       stock if available."""
    base_earnings_url = 'https://finance.yahoo.com/calendar/earnings'
    if offset >= count:
        return []
    temp = pd.Timestamp(date)
    date = temp.strftime('%Y-%m-%d')
    dated_url = '{0}?day={1}&offset={2}&size={3}'.format(base_earnings_url, date, offset, 100)
    result = _parse_earnings_json(dated_url)
    stores = result['context']['dispatcher']['stores']
    earnings_count = stores['ScreenerCriteriaStore']['meta']['total']
    new_offset = offset + 100
    more_earnings = get_earnings_for_date(date, new_offset, earnings_count)
    current_earnings = stores['ScreenerResultsStore']['results']['rows']
    total_earnings = current_earnings + more_earnings
    return total_earnings