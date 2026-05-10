def get_top_crypto():
    """Gets the top 100 Cryptocurrencies by Market Cap"""
    session = HTMLSession()
    resp = session.get('https://finance.yahoo.com/cryptocurrencies?offset=0&count=100')
    tables = pd.read_html(resp.html.raw_html)
    df = tables[0].copy()
    df['% Change'] = df['% Change'].map(lambda x: float(str(x).strip('%').strip('+').replace(',', '')))
    del df['52 Week Range']
    del df['1 Day Chart']
    fields_to_change = [x for x in df.columns.tolist() if 'Volume' in x or x == 'Market Cap' or x == 'Circulating Supply']
    for field in fields_to_change:
        if type(df[field][0]) == str:
            df[field] = df[field].map(lambda x: _convert_to_numeric(str(x)))
    session.close()
    return df