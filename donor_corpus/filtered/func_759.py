def apply_to_sample(f, sample):
    if hasattr(sample, '__len__') and len(sample) == 0:
        return {}

    def _apply(x):
        if torch.is_tensor(x):
            return f(x)
        elif isinstance(x, dict):
            return {key: _apply(value) for key, value in x.items()}
        elif isinstance(x, list):
            return [_apply(x) for x in x]
        elif isinstance(x, tuple):
            return tuple((_apply(x) for x in x))
        elif isinstance(x, set):
            return {_apply(x) for x in x}
        else:
            return x
    return _apply(sample)