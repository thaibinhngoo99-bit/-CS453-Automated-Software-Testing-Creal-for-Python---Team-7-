def call_run(run_fn):
    import numpy as np
    params = NS.from_dict(json.loads(sys.stdin.read()))

    def load_data(name, path):
        if isinstance(path, str) and data_keys.match(name):
            return (name, np.load(path, allow_pickle=True))
        return (name, path)
    print(params.dataset)
    ds = NS.walk(params.dataset, load_data)
    config = params.config
    config.framework_params = NS.dict(config.framework_params)
    try:
        result = run_fn(ds, config)
        res = dict(result)
        for name in ['predictions', 'truth', 'probabilities']:
            arr = result[name]
            if arr is not None:
                res[name] = os.path.join(config.result_dir, '.'.join([name, 'npy']))
                np.save(res[name], arr, allow_pickle=True)
    except Exception as e:
        log.exception(e)
        res = dict(error_message=str(e), models_count=0)
    print(config.result_token)
    print(json.dumps(res, separators=(',', ':')))