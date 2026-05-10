def init_state():
    state = 0
    RPIO.setup(loud1, RPIO.OUT)
    RPIO.setup(loud2, RPIO.OUT)