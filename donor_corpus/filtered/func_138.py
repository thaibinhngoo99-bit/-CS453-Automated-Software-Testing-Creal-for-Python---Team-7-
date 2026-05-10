def xform_4(g, A):
    """
    Basis xform for 4-tensor
    """
    if len(g.shape) != 4:
        raise Exception('\n            Dimension error: arg1 should be a four-tensor.\n            Note that you should set is_fitted to be False.\n        ')
    return xform.xform_4_np(g, A)