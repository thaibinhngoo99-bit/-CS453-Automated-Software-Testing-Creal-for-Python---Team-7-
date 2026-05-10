def get_live_price(ticker):
    """Gets the live price of input ticker
    
       @param: ticker
    """
    df = get_data(ticker, end_date=pd.Timestamp.today() + pd.DateOffset(10))
    return df.close[-1]