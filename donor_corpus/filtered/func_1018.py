@override_native_generic_func('roi_align_strategy')
def roi_align_strategy(attrs, inputs, out_type, target):
    """roi_align generic strategy"""
    strategy = _op.OpStrategy()
    layout = attrs.layout
    assert layout == 'NCHW', 'only support nchw for now'
    strategy.add_implementation(wrap_compute_roi_align(topi.vision.rcnn.roi_align_nchw), wrap_topi_schedule(topi.generic.schedule_roi_align), name='roi_align.generic')
    return strategy