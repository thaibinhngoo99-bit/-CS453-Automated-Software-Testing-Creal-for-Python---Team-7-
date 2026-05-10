def encrypt_month(value_, params=None):
    date = arrow.get(value_)
    date_str = date.format('YYYY-MM-DD')
    return __mask_month(date_str)