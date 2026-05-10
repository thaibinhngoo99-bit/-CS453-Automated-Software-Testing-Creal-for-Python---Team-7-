def get_segments(source, length, count):
    begins = []
    l = len(source)
    for _ in range(count):
        begins.append(randint(0, l - length - 1))
    segments = []
    for begin in begins:
        segments.append(source[begin:begin + length])
    return segments