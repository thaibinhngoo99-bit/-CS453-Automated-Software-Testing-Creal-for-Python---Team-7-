def set_add_reduce(ops):
    """
    Set the add_reduce method on the LogOperations instance.

    """
    base = ops.base
    if base == 2:

        def add_reduce(self, x, axis=None, func=np.logaddexp2):
            if len(x) == 0:
                z = self.zero
            else:
                z = func.reduce(x, axis=axis, dtype=float)
            return z
    elif base == 'e' or np.isclose(base, np.e):

        def add_reduce(self, x, axis=None, func=np.logaddexp):
            if len(x) == 0:
                z = self.zero
            else:
                z = func.reduce(x, axis=axis, dtype=float)
            return z
    else:

        def add_reduce(self, x, axis=None):
            if len(x) == 0:
                z = self.zero
            else:
                x2 = x * np.log2(base)
                z = np.logaddexp2.reduce(x2, axis=axis, dtype=float)
                z /= np.log2(base)
            return z
    add_reduce.__doc__ = "\n    Performs an `addition' reduction on `x`.\n\n    Assumption: :math:`y <= 0`.\n\n    Returns\n    -------\n    z : float\n        The summation of the elements in `x`.\n\n    "
    ops.add_reduce = MethodType(add_reduce, ops)