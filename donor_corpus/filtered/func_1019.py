def wrap_compute_proposal(topi_compute):
    """wrap proposal topi compute"""

    def _compute_proposal(attrs, inputs, out_type):
        scales = get_float_tuple(attrs.scales)
        ratios = get_float_tuple(attrs.ratios)
        feature_stride = attrs.feature_stride
        threshold = attrs.threshold
        rpn_pre_nms_top_n = attrs.rpn_pre_nms_top_n
        rpn_post_nms_top_n = attrs.rpn_post_nms_top_n
        rpn_min_size = attrs.rpn_min_size
        iou_loss = bool(get_const_int(attrs.iou_loss))
        return [topi_compute(inputs[0], inputs[1], inputs[2], scales, ratios, feature_stride, threshold, rpn_pre_nms_top_n, rpn_post_nms_top_n, rpn_min_size, iou_loss)]
    return _compute_proposal