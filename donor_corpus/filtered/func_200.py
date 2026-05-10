def get_quote_table(ticker, dict_result=True, headers={'User-agent': 'Mozilla/5.0'}):
    """Scrapes data elements found on Yahoo Finance's quote page 
       of input ticker
    
       @param: ticker
       @param: dict_result = True
    """
    site = 'https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker
    tables = pd.read_html(requests.get(site, headers=headers).text)
    data = tables[0].append(tables[1])
    data.columns = ['attribute', 'value']
    quote_price = pd.DataFrame(['Quote Price', get_live_price(ticker)]).transpose()
    quote_price.columns = data.columns.copy()
    data = data.append(quote_price)
    data = data.sort_values('attribute')
    data = data.drop_duplicates().reset_index(drop=True)
    data['value'] = data.value.map(force_float)
    if dict_result:
        result = {key: val for key, val in zip(data.attribute, data.value)}
        return result
    return data