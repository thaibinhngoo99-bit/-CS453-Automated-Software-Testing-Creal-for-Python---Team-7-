def handle_sign(qq):
    last_sign = data.get(qq, 'last_sign')
    now = timestamp_now()
    msg = ''
    if is_same_day(last_sign, now):
        info = data.get(qq, 'last_sign_info')
        msg = lang.already_sign
    else:
        msg = lang.sign_success
        info = gen_sign_info()
        data.set(qq, 'last_sign', now)
        data.set(qq, 'last_sign_info', info)
    msg += lang.sign % (natural_date(last_sign), info['rp'])
    return msg