def read_references(reporter, ref_path):
    """Read shared file of reference links, returning dictionary of valid references
    {symbolic_name : URL}
    """
    if not ref_path:
        raise Warning('No filename has been provided.')
    result = {}
    urls_seen = set()
    with open(ref_path, 'r') as reader:
        for num, line in enumerate(reader, 1):
            if P_INTERNAL_INCLUDE_LINK.search(line):
                continue
            m = P_INTERNAL_LINK_DEF.search(line)
            message = '{}: {} not a valid reference: {}'
            require(m, message.format(ref_path, num, line.rstrip()))
            name = m.group(1)
            url = m.group(2)
            message = 'Empty reference at {0}:{1}'
            require(name, message.format(ref_path, num))
            unique_name = name not in result
            unique_url = url not in urls_seen
            reporter.check(unique_name, ref_path, 'Duplicate reference name {0} at line {1}', name, num)
            reporter.check(unique_url, ref_path, 'Duplicate definition of URL {0} at line {1}', url, num)
            result[name] = url
            urls_seen.add(url)
    return result