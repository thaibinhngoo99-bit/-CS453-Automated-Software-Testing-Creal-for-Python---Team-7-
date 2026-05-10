def set_add(ops):
    """
    Set the add method on the LogOperations instance.

    """
    base = ops.base
    if base == 2:

        def add(self, x, y, func=np.logaddexp2):
            return func(x, y)
    elif base == 'e' or np.isclose(base, np.e):

        def add(self, x, y, func=np.logaddexp):
            return func(x, y)
    else:

        def add(self, x, y):
            x2 = x * np.log2(base)
            y2 = y * np.log2(base)
            z = np.logaddexp2(x2, y2)
            z *= self.log(2)
            return z
    add.__doc__ = '\n    Add the arrays element-wise.  Neither x nor y will be modified.\n\n    Assumption: y <= 0.\n\n    Parameters\n    ----------\n    x, y : NumPy arrays, shape (n,)\n        The arrays to add.\n\n    Returns\n    -------\n    z : NumPy array, shape (n,)\n        The resultant array.\n\n    '
    ops.add = MethodType(add, ops)