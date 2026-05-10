def timestamp(time=None, format=TIMESTAMP_FORMAT):
    if not time:
        time = datetime.utcnow()
    if isinstance(time, six.integer_types + (float,)):
        time = datetime.fromtimestamp(time)
    return time.strftime(format)