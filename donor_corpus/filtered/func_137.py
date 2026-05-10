def xform_2(H, A):
    """
    Basis xform for 2-tensor
    """
    if len(H.shape) != 2:
        raise Exception('Dimension error: arg1 should be a matrix')
    return A.T @ H @ A