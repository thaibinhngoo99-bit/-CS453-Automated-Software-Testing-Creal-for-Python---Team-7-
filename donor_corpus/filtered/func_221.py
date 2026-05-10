def get_earnings_in_date_range(start_date, end_date):
    """Inputs: @start_date
                   @end_date
                   
           Returns the stock tickers with expected EPS data for all dates in the
           input range (inclusive of the start_date and end_date."""
    earnings_data = []
    days_diff = pd.Timestamp(end_date) - pd.Timestamp(start_date)
    days_diff = days_diff.days
    current_date = pd.Timestamp(start_date)
    dates = [current_date + datetime.timedelta(diff) for diff in range(days_diff + 1)]
    dates = [d.strftime('%Y-%m-%d') for d in dates]
    i = 0
    while i < len(dates):
        try:
            earnings_data += get_earnings_for_date(dates[i])
        except Exception:
            pass
        i += 1
    return earnings_data