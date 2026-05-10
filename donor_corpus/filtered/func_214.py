def get_dividends(ticker, start_date=None, end_date=None, index_as_date=True, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}):
    """Downloads historical dividend data into a pandas data frame.
    
       @param: ticker
       @param: start_date = None
       @param: end_date = None
       @param: index_as_date = True
    """
    site, params = build_url(ticker, start_date, end_date, '1d')
    resp = requests.get(site, params=params, headers=headers)
    if not resp.ok:
        return pd.DataFrame()
    data = resp.json()
    if 'events' not in data['chart']['result'][0] or 'dividends' not in data['chart']['result'][0]['events']:
        return pd.DataFrame()
    frame = pd.DataFrame(data['chart']['result'][0]['events']['dividends'])
    frame = frame.transpose()
    frame.index = pd.to_datetime(frame.index, unit='s')
    frame.index = frame.index.map(lambda dt: dt.floor('d'))
    frame = frame.sort_index()
    frame['ticker'] = ticker.upper()
    frame = frame.drop(columns='date')
    frame = frame.rename({'amount': 'dividend'}, axis='columns')
    if not index_as_date:
        frame = frame.reset_index()
        frame.rename(columns={'index': 'date'}, inplace=True)
    return frame