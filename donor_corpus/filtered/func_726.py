def disable_all_timers():
    print('disabling all the timers')
    global timer
    try:
        timer.cancel()
        print('timer canceled')
    except:
        pass