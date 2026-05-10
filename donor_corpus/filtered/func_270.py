def manage_timestamps(segment):
    try:
        st, et = (segment[5], segment[6])
    except:
        st = segment[5]
        return [st]
    try:
        delete_timestamps = segment[7]
    except:
        return [st, et]
    if not delete_timestamps:
        return [st, et]
    else:
        return [st] + [t for s in delete_timestamps.split(',') for t in (s.split('-')[0], s.split('-')[1])] + [et]