def debug(*args, **kwargs):
    output = ''
    for x in args:
        print(x)
        output += str(x)
    return output