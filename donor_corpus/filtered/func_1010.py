@override_native_generic_func('multibox_prior_strategy')
def multibox_prior_strategy(attrs, inputs, out_type, target):
    """multibox_prior generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_multibox_prior(topi.vision.ssd.multibox_prior), wrap_topi_schedule(topi.generic.schedule_multibox_prior), name='multibox_prior.generic')
    return strategy