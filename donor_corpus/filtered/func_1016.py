@override_native_generic_func('non_max_suppression_strategy')
def nms_strategy(attrs, inputs, out_type, target):
    """nms generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_nms(topi.vision.non_max_suppression), wrap_topi_schedule(topi.generic.schedule_nms), name='nms.generic')
    return strategy