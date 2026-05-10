def btn_trans(a, edge):
    global state
    global timer
    print('Button: %s , edge: %s, state: %d' % (str(a), str(edge), state))
    if edge and state is 0:
        state = 1
        timer = Timer(t1_2, time1_trans).start()
    elif not edge and (state is 1 or state is 4 or state is 2):
        state = 0
        disable_all_timers()
        stop_sirene1()
        stop_sirene2()
        try:
            play_next()
        except:
            tell_gobbelz('Cannot play next song. Sorry:(')
            tell_gobbelz('Bailing out')
            sys.exit(1)
    elif not edge and state is 5:
        print('button released while removing music, all fine')
    else:
        print('this should never happen')