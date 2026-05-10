@hps.composite
def generalized_paretos(draw, batch_shape=None):
    if batch_shape is None:
        batch_shape = draw(tfp_hps.shapes())
    constraints = dict(loc=tfp_hps.identity_fn, scale=tfp_hps.softplus_plus_eps(), concentration=lambda x: tf.math.tanh(x) * 0.24)
    params = draw(tfp_hps.broadcasting_params(batch_shape, params_event_ndims=dict(loc=0, scale=0, concentration=0), constraint_fn_for=constraints.get))
    dist = tfd.GeneralizedPareto(validate_args=draw(hps.booleans()), **params)
    if dist.batch_shape != batch_shape:
        raise AssertionError('batch_shape mismatch: expect {} but got {}'.format(batch_shape, dist))
    return dist