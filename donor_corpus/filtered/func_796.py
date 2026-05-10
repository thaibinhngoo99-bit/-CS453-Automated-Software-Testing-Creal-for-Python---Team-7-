@lru_cache(maxsize=999)
def load_bar_data(vt_symbol: str, interval: Interval, start: datetime, end: datetime):
    """"""
    symbol, exchange = extract_vt_symbol(vt_symbol)
    return database_manager.load_bar_data(symbol, exchange, interval, start, end)