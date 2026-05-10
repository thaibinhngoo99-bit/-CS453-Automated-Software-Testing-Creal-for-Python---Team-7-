def run_hook(name, *args):
    results = []
    f_list = hooks.get(name, [])
    for p, f in f_list:
        if p.is_enabled():
            try:
                r = f(*args)
            except Exception:
                _logger.exception(f'Plugin error. plugin: {p}, hook: {name}')
                r = False
            if r:
                results.append(r)
    if results:
        assert len(results) == 1, results
        return results[0]