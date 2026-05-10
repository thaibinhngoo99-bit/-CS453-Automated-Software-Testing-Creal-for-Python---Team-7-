def _parse_compile_spec(compile_spec: Dict[str, Any]) -> trtorch._C.CompileSpec:
    info = trtorch._C.CompileSpec()
    if 'input_shapes' not in compile_spec:
        raise KeyError('Input shapes for inputs are required as a List, provided as either a static sizes or a range of three sizes (min, opt, max) as Dict')
    info.input_ranges = _parse_input_ranges(compile_spec['input_shapes'])
    if 'op_precision' in compile_spec:
        info.op_precision = _parse_op_precision(compile_spec['op_precision'])
    if 'refit' in compile_spec:
        assert isinstance(compile_spec['refit'], bool)
        info.refit = compile_spec['refit']
    if 'debug' in compile_spec:
        assert isinstance(compile_spec['debug'], bool)
        info.debug = compile_spec['debug']
    if 'strict_types' in compile_spec:
        assert isinstance(compile_spec['strict_types'], bool)
        info.strict_types = compile_spec['strict_types']
    if 'allow_gpu_fallback' in compile_spec:
        assert isinstance(compile_spec['allow_gpu_fallback'], bool)
        info.allow_gpu_fallback = compile_spec['allow_gpu_fallback']
    if 'device_type' in compile_spec:
        info.device = _parse_device_type(compile_spec['device_type'])
    if 'capability' in compile_spec:
        assert isinstance(compile_spec['capability'], _types.EngineCapability)
        info.capability = compile_spec['capability']
    if 'num_min_timing_iters' in compile_spec:
        assert type(compile_spec['num_min_timing_iters']) is int
        info.num_min_timing_iters = compile_spec['num_min_timing_iters']
    if 'num_avg_timing_iters' in compile_spec:
        assert type(compile_spec['num_avg_timing_iters']) is int
        info.num_avg_timing_iters = compile_spec['num_avg_timing_iters']
    if 'workspace_size' in compile_spec:
        assert type(compile_spec['workspace_size']) is int
        info.workspace_size = compile_spec['workspace_size']
    if 'max_batch_size' in compile_spec:
        assert type(compile_spec['max_batch_size']) is int
        info.max_batch_size = compile_spec['max_batch_size']
    return info