def bitreverse(x):
    y = 0
    for i in range(8):
        if x >> 7 - i & 1 == 1:
            y |= 1 << i
    return y