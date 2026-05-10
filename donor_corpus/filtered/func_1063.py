def update():
    global logo_time
    if logo_time > 1.0:
        logo_time = 0.8
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.05