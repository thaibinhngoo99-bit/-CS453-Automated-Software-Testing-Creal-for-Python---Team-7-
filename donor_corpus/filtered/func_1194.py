def sample_balanced_positive_negative(indicator, sample_size, labels, positive_fraction=0.5):
    """Subsamples minibatches to a desired balance of positives and negatives.

    Arguments:

    - *indicator*: boolean tensor of shape [N] whose True entries can be sampled.
    - *sample_size*: desired batch size. If None, keeps all positive samples and
        randomly selects negative samples so that the positive sample fraction
        matches positive_fraction.
    - *labels*: boolean tensor of shape [N] denoting positive(=True) and negative
        (=False) examples.
    - *positive_fraction*: desired fraction of positive examples (scalar in [0,1])
        in the batch.

    Returns:

    *sampled_idx_indicator*: boolean tensor of shape [N], True for entries which are sampled.
    """
    negative_idx = tf.logical_not(labels)
    positive_idx = tf.logical_and(labels, indicator)
    negative_idx = tf.logical_and(negative_idx, indicator)
    if sample_size is None:
        max_num_pos = tf.reduce_sum(tf.cast(positive_idx, dtype=tf.int32))
    else:
        max_num_pos = int(positive_fraction * sample_size)
    sampled_pos_idx = subsample_indicator(positive_idx, max_num_pos)
    num_sampled_pos = tf.reduce_sum(tf.cast(sampled_pos_idx, tf.int32))
    if sample_size is None:
        negative_positive_ratio = (1 - positive_fraction) / positive_fraction
        max_num_neg = tf.cast(negative_positive_ratio * tf.cast(num_sampled_pos, dtype=tf.float32), dtype=tf.int32)
    else:
        max_num_neg = sample_size - num_sampled_pos
    sampled_neg_idx = subsample_indicator(negative_idx, max_num_neg)
    return tf.logical_or(sampled_pos_idx, sampled_neg_idx)