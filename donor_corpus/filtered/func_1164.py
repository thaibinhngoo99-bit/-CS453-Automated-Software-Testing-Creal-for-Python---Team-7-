def logged(func):
    print('Adding logging to', func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('You called', func.__name__)
        return func(*args, **kwargs)
    return wrapper