def get_company_info(ticker):
    """Scrape the company information for a ticker

       @param: ticker
    """
    site = f'https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}'
    json_info = _parse_json(site)
    json_info = json_info['assetProfile']
    info_frame = pd.DataFrame.from_dict(json_info, orient='index', columns=['Value'])
    info_frame = info_frame.drop('companyOfficers', axis='index')
    info_frame.index.name = 'Breakdown'
    return info_frame