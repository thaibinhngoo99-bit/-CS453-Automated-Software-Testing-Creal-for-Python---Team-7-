def _raw_get_daily_info(site):
    session = HTMLSession()
    resp = session.get(site)
    tables = pd.read_html(resp.html.raw_html)
    df = tables[0].copy()
    df.columns = tables[0].columns
    del df['52 Week Range']
    df['% Change'] = df['% Change'].map(lambda x: float(x.strip('%+').replace(',', '')))
    fields_to_change = [x for x in df.columns.tolist() if 'Vol' in x or x == 'Market Cap']
    for field in fields_to_change:
        if type(df[field][0]) == str:
            df[field] = df[field].map(_convert_to_numeric)
    session.close()
    return df