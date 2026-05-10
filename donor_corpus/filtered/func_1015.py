def wrap_compute_nms(topi_compute):
    """wrap nms topi compute"""

    def _compute_nms(attrs, inputs, out_type):
        max_output_size = inputs[3]
        iou_threshold = inputs[4]
        if attrs.max_output_size is not None:
            max_output_size = attrs.max_output_size
        if attrs.iou_threshold is not None:
            iou_threshold = get_const_float(attrs.iou_threshold)
        return_indices = bool(get_const_int(attrs.return_indices))
        force_suppress = bool(get_const_int(attrs.force_suppress))
        top_k = get_const_int(attrs.top_k)
        coord_start = get_const_int(attrs.coord_start)
        score_index = get_const_int(attrs.score_index)
        id_index = get_const_int(attrs.id_index)
        invalid_to_bottom = bool(get_const_int(attrs.invalid_to_bottom))
        if return_indices:
            return topi_compute(inputs[0], inputs[1], inputs[2], max_output_size, iou_threshold, force_suppress, top_k, coord_start, score_index, id_index, return_indices, invalid_to_bottom)
        return [topi_compute(inputs[0], inputs[1], inputs[2], max_output_size, iou_threshold, force_suppress, top_k, coord_start, score_index, id_index, return_indices, invalid_to_bottom)]
    return _compute_nms