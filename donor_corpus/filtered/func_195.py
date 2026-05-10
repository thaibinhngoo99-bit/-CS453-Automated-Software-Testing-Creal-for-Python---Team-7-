def tickers_ibovespa(include_company_data=False):
    """Downloads list of currently traded tickers on the Ibovespa, Brazil"""
    table = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_companhias_citadas_no_Ibovespa')[0]
    table.columns = ['Symbol', 'Share', 'Sector', 'Type', 'Site']
    if include_company_data:
        return table
    ibovespa_tickers = sorted(table.Symbol.tolist())
    return ibovespa_tickers