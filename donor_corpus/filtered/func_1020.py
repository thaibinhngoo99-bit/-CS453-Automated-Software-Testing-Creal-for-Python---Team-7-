@override_native_generic_func('proposal_strategy')
def proposal_strategy(attrs, inputs, out_type, target):
    """proposal generic strategy"""
    strategy = _op.OpStrategy()
    strategy.add_implementation(wrap_compute_proposal(topi.vision.rcnn.proposal), wrap_topi_schedule(topi.generic.schedule_proposal), name='proposal.generic')
    return strategy