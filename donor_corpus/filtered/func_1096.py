def handle_night(qq):
    last_morning = data.get(qq, 'last_morning')
    last_night = data.get(qq, 'last_night')
    now = timestamp_now()
    if last_night > last_morning:
        msg = lang.no_getup
    else:
        data.set(qq, 'last_night', now)
        msg = lang.night_success % natural_time(now - last_morning)
    return msg