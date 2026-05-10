def time2_trans():
    global state
    global timer
    if state is 2:
        state = 4
        start_sirene2()
        timer = Timer(t4_5, time3_trans).start()
    else:
        print('State is not 2, will do nothing')