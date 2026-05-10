def time1_trans():
    global state
    global timer
    if state is 1:
        state = 2
        start_sirene1()
        timer = Timer(t2_4, time2_trans).start()
    else:
        print('State is not 1, will do nothing')