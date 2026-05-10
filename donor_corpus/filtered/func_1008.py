@override_native_generic_func('topk_strategy')
def topk_strategy(attrs, inputs, out_type, target):
    """topk generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_topk(topi.topk), wrap_topi_schedule(topi.generic.schedule_topk), name='topk.generic')
    return strategy