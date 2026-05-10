def handle_morning(qq):
    last_morning = data.get(qq, 'last_morning')
    last_night = data.get(qq, 'last_night')
    now = timestamp_now()
    if last_morning > last_night:
        msg = lang.no_sleep
    else:
        msg = lang.morning_success % natural_time(now - last_night)
        data.set(qq, 'last_morning', now)
    return msg