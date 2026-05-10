def get_splits(ticker, start_date=None, end_date=None, index_as_date=True, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}):
    """Downloads historical stock split data into a pandas data frame.
    
       @param: ticker
       @param: start_date = None
       @param: end_date = None
       @param: index_as_date = True
    """
    site, params = build_url(ticker, start_date, end_date, '1d')
    resp = requests.get(site, params=params, headers=headers)
    if not resp.ok:
        raise AssertionError(resp.json())
    data = resp.json()
    if 'events' not in data['chart']['result'][0]:
        raise AssertionError('There is no data available on stock events, or none have occured')
    if 'splits' not in data['chart']['result'][0]['events']:
        raise AssertionError('There is no data available on stock splits, or none have occured')
    frame = pd.DataFrame(data['chart']['result'][0]['events']['splits'])
    frame = frame.transpose()
    frame.index = pd.to_datetime(frame.index, unit='s')
    frame.index = frame.index.map(lambda dt: dt.floor('d'))
    frame = frame.sort_index()
    frame['ticker'] = ticker.upper()
    frame = frame.drop(columns=['date', 'denominator', 'numerator'])
    if not index_as_date:
        frame = frame.reset_index()
        frame.rename(columns={'index': 'date'}, inplace=True)
    return frame