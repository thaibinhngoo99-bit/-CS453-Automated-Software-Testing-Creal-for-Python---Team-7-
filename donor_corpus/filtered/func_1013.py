def wrap_compute_get_valid_counts(topi_compute):
    """wrap get_valid_counts topi compute"""

    def _compute_get_valid_counts(attrs, inputs, out_type):
        score_threshold = inputs[1]
        id_index = get_const_int(attrs.id_index)
        score_index = get_const_int(attrs.score_index)
        if attrs.score_threshold is not None:
            score_threshold = get_const_float(attrs.score_threshold)
        return topi_compute(inputs[0], score_threshold, id_index, score_index)
    return _compute_get_valid_counts