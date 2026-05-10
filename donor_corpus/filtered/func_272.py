def to_cut_yaml(inmp4, outmp4, ymlname, timestamps):

    def pairwise(iterable):
        """s -> (s0, s1), (s2, s3), (s4, s5), ..."""
        a = iter(iterable)
        return list(zip(a, a))
    timestamps = [to_cut_fmt(t) for t in timestamps]
    timeframe = []
    if len(timestamps) == 1:
        timeframe = [{'from': 'start', 'to': timestamps[0]}]
    else:
        for s, e in pairwise(['start'] + timestamps + ['end']):
            timeframe += [{'from': s, 'to': e}]
    out = {'input': inmp4, 'output': outmp4, 'cut_method': 'delete', 'timeframe': timeframe}
    with open(ymlname, 'w') as fd:
        yaml.dump(out, fd, default_flow_style=False, sort_keys=False)