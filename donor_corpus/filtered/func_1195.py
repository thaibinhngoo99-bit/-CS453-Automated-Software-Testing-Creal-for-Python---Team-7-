def batch_sample_balanced_positive_negative(indicators, sample_size, labels, positive_fraction=0.5, dtype=tf.float32):
    """Subsamples minibatches to a desired balance of positives and negatives.

    Arguments:

    - *indicator*: boolean tensor of shape [batch_size, N] whose True entries can be sampled.
    - *sample_size*: desired batch size. If None, keeps all positive samples and
        randomly selects negative samples so that the positive sample fraction
        matches positive_fraction.
    - *labels*: boolean tensor of shape [batch_size, N] denoting positive(=True) and negative
        (=False) examples.
    - *positive_fraction*: desired fraction of positive examples (scalar in [0,1])
        in the batch.

    Returns:

    A boolean tensor of shape [M, N], True for entries which are sampled.
    """

    def _minibatch_subsample_fn(inputs):
        indicators, targets = inputs
        return sample_balanced_positive_negative(tf.cast(indicators, tf.bool), sample_size, tf.cast(targets, tf.bool), positive_fraction=positive_fraction)
    return tf.cast(tf.map_fn(_minibatch_subsample_fn, [indicators, labels], dtype=tf.bool, parallel_iterations=16, back_prop=True), dtype=dtype)