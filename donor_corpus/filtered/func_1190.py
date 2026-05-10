def colorizer_enabled(function):
    """do not colorize if it's not enabled"""

    def wrapper(*args):
        if ENABLE_COLORIZER:
            return function(*args)
        elif args:
            return args[0]
        else:
            return args
    return wrapper