def format_timestamp_args(timestamps):
    if len(timestamps) == 1:
        return [f'-ss {timestamps[0]} ']

    def pairwise(iterable):
        """s -> (s0, s1), (s2, s3), (s4, s5), ..."""
        a = iter(iterable)
        return list(zip(a, a))
    cmds = [f'-ss {s} -to {e}' for s, e in pairwise(timestamps)]
    return cmds