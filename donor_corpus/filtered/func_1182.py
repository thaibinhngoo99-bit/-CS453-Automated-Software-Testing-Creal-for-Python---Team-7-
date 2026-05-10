def TradingAlorythm(command, market, amount, coinname, step, stoploss, key, secret):
    TestTrading = Bittrex(key, secret)
    period = timedelta(seconds=20)
    next_tick = datetime.now() + period
    seconds = 20
    firstCycle = True
    if command == 'y':
        print('buying {0} of {1} coins'.format(amount, coinname))
    while command == 'y':
        if next_tick <= datetime.now():
            print('Connecting to Bittrex')
            seconds += 20
            next_tick += period
            print('Timer ticked')
            print('Updating stock exchange...')
            t = TestTrading.get_ticker(market)
            balance = TestTrading.get_balance(coinname)
            orders = TestTrading.get_open_orders(market)
            a = json.dumps(t)
            print(t)
            print('Balance is {} '.format(balance['result']['Available']))
            print(orders)
            bid = t['result']['Bid']
            ask = t['result']['Ask']
            last = t['result']['Last']
            if firstCycle:
                StartValue = bid
                firstCycle = False
            Stop_loss = StartValue - 7e-08
            print('*--------------------------')
            print('| Start Value  | {: .8f} '.format(StartValue))
            print('| Stop loss    | {: .8f} '.format(Stop_loss))
            print('|--------------------------')
            print('| Bid          | {: .8f} '.format(bid))
            print('| Ask          | {: .8f} '.format(ask))
            print('| Last         | {: .8f} '.format(last))
            print('*--------------------------')
            if bid >= step + StartValue:
                print('MOVE STOP-LOSS')
                StartValue = bid
            if bid <= stoploss:
                print('Sell order sent')