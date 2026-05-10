def build_url(ticker, start_date=None, end_date=None, interval='1d'):
    if end_date is None:
        end_seconds = int(pd.Timestamp('now').timestamp())
    else:
        end_seconds = int(pd.Timestamp(end_date).timestamp())
    if start_date is None:
        start_seconds = 7223400
    else:
        start_seconds = int(pd.Timestamp(start_date).timestamp())
    site = base_url + ticker
    params = {'period1': start_seconds, 'period2': end_seconds, 'interval': interval.lower(), 'events': 'div,splits'}
    return (site, params)