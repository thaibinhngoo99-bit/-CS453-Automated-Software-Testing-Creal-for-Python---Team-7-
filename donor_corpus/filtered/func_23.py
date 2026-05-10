def _parse_input_ranges(input_sizes: List) -> List:
    if any((not isinstance(i, dict) and (not _supported_input_size_type(i)) for i in input_sizes)):
        raise KeyError('An input size must either be a static size or a range of three sizes (min, opt, max) as Dict')
    parsed_input_sizes = []
    for i in input_sizes:
        if isinstance(i, dict):
            if all((k in i for k in ['min', 'opt', 'min'])):
                in_range = trtorch._C.InputRange()
                in_range.min = i['min']
                in_range.opt = i['opt']
                in_range.max = i['max']
                parsed_input_sizes.append(in_range)
            elif 'opt' in i:
                in_range = trtorch._C.InputRange()
                in_range.min = i['opt']
                in_range.opt = i['opt']
                in_range.max = i['opt']
                parsed_input_sizes.append(in_range)
            else:
                raise KeyError('An input size must either be a static size or a range of three sizes (min, opt, max) as Dict')
        elif isinstance(i, list):
            in_range = trtorch._C.InputRange()
            in_range.min = i
            in_range.opt = i
            in_range.max = i
            parsed_input_sizes.append(in_range)
        elif isinstance(i, tuple):
            in_range = trtorch._C.InputRange()
            in_range.min = list(i)
            in_range.opt = list(i)
            in_range.max = list(i)
            parsed_input_sizes.append(in_range)
    return parsed_input_sizes