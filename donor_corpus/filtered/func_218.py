def get_next_earnings_date(ticker):
    base_earnings_url = 'https://finance.yahoo.com/quote'
    new_url = base_earnings_url + '/' + ticker
    parsed_result = _parse_earnings_json(new_url)
    temp = parsed_result['context']['dispatcher']['stores']['QuoteSummaryStore']['calendarEvents']['earnings']['earningsDate'][0]['raw']
    return datetime.datetime.fromtimestamp(temp)