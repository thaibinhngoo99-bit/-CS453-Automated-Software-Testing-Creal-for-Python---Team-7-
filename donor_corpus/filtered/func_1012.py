@override_native_generic_func('multibox_transform_loc_strategy')
def multibox_transform_loc_strategy(attrs, inputs, out_type, target):
    """schedule multibox_transform_loc"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_multibox_transform_loc(topi.vision.ssd.multibox_transform_loc), wrap_topi_schedule(topi.generic.schedule_multibox_transform_loc), name='multibox_transform_loc.generic')
    return strategy