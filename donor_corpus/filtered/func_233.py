def symbol_prompt():
    exchange = dev_5_vwap_config_map.get('exchange').value
    example = EXAMPLE_PAIRS.get(exchange)
    return 'Enter the trading pair you would like to trade on %s%s >>> ' % (exchange, f' (e.g. {example})' if example else '')