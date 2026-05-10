def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b[len(b) - len(a):] == a, a[len(a) - len(b):] == b)[len(a) >= len(b)]