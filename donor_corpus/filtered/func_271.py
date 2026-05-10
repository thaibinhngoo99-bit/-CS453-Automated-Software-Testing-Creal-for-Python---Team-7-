def to_cut_fmt(timestamp):
    out = ''
    labels = ['h', 'm', 's']
    lb_idx = 0
    for c in timestamp:
        if c == ':':
            out += labels[lb_idx]
            lb_idx += 1
        else:
            out += c
    return out