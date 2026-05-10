def measureTime():
    global lasttime
    currentTime = time.time()
    diff = currentTime - lasttime
    lasttime = currentTime
    return diff