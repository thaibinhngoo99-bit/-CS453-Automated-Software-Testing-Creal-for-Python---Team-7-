def set_add_inplace(ops):
    """
    Set the add_inplace method on the LogOperations instance.

    """
    base = ops.base
    if base == 2:

        def add_inplace(self, x, y, func=np.logaddexp2):
            return func(x, y, x)
    elif base == 'e' or np.isclose(base, np.e):

        def add_inplace(self, x, y, func=np.logaddexp):
            return func(x, y, x)
    else:

        def add_inplace(self, x, y):
            x *= np.log2(base)
            y2 = y * np.log2(base)
            np.logaddexp2(x, y2, x)
            x *= self.log(2)
            return x
    add_inplace.__doc__ = '\n    Adds `y` to `x`, in-place.  `x` will be modified, but `y` will not.\n\n    Assumption: :math:`y <= 0`.\n\n    Parameters\n    ----------\n    x, y : NumPy arrays, shape (n,)\n        The arrays to add.\n\n    Returns\n    -------\n    x : NumPy array, shape (n,)\n        The resultant array.\n\n    '
    ops.add_inplace = MethodType(add_inplace, ops)