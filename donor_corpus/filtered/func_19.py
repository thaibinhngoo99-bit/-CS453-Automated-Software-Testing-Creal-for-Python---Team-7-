def create_checker(args, filename, info):
    """Create appropriate checker for file."""
    for pat, cls in CHECKERS:
        if pat.search(filename):
            return cls(args, filename, **info)
    return NotImplemented