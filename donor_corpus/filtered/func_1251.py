def checksum(data):
    if len(data) & 1:
        data += b'\x00'
    cs = 0
    for pos in range(0, len(data), 2):
        b1 = data[pos]
        b2 = data[pos + 1]
        cs += (b1 << 8) + b2
    while cs >= 65536:
        cs = (cs & 65535) + (cs >> 16)
    cs = ~cs & 65535
    return cs