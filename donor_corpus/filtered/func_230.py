def get_company_officers(ticker):
    """Scrape the company information and return a table of the officers

       @param: ticker
    """
    site = f'https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}'
    json_info = _parse_json(site)
    json_info = json_info['assetProfile']['companyOfficers']
    info_frame = pd.DataFrame.from_dict(json_info)
    info_frame = info_frame.set_index('name')
    return info_frame