import json
from datetime import datetime, timedelta
from bittrex.bittrex import Bittrex


def TradingAlorythm(command, market, amount, coinname, step, stoploss, key, secret):
    TestTrading = Bittrex(key, secret)
    period = timedelta(seconds=20)
    next_tick = datetime.now() + period
    seconds = 20
    firstCycle = True
    if command == "y":
        print("buying {0} of {1} coins".format(amount, coinname))
        # раскомментировать для созадния ордера на покупку
        # TestTrading.buy_limit(market, amount, coinprice)

    while command == "y":
        # таймер каждые 20 секунд
        if next_tick <= datetime.now():
            print("Connecting to Bittrex")
            seconds += 20
            next_tick += period
            print("Timer ticked")
            print("Updating stock exchange...")
            # Считываем значения курса
            t = TestTrading.get_ticker(market)
            # Запрашиваем баланс
            balance = TestTrading.get_balance(coinname)
            # Запрашиваем текущие ордера
            orders = TestTrading.get_open_orders(market)
            a = json.dumps(t)
            # Печатаем значения курса
            print(t)
            # Печатаем баланс
            print("Balance is {} ".format(balance['result']['Available']))
            # Печатаем ордера
            print(orders)
            # Раскладываем по переменным
            bid = t['result']['Bid']
            ask = t['result']['Ask']
            last = t['result']['Last']
            if firstCycle:
                StartValue = bid
                firstCycle = False
            Stop_loss = StartValue - 0.00000007
            print("*--------------------------")
            print("| Start Value  | {: .8f} ".format(StartValue))
            print("| Stop loss    | {: .8f} ".format(Stop_loss))
            print("|--------------------------")
            print("| Bid          | {: .8f} ".format(bid))
            print("| Ask          | {: .8f} ".format(ask))
            print("| Last         | {: .8f} ".format(last))
            print("*--------------------------")
            # Добавляем Bid в конец массива
            # A.append(float(bid))
            if bid >= step + StartValue:
                print("MOVE STOP-LOSS")
                StartValue = bid

            if bid <= stoploss:
                print("Sell order sent")