def parse(s: str) -> Tuple[List[str], Dict[Tuple[str, str], str]]:
    lines = s.splitlines()
    initial = list(lines[0].strip())
    mapping = {}
    for line in lines[2:]:
        if (stripped_line := line.strip()):
            left, right = stripped_line.split(' -> ', 1)
            mapping[left[0], left[1]] = right
    return (initial, mapping)