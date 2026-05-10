def exp_func(b):
    """
    Returns a base-`b` exponential function.

    Parameters
    ----------
    b : positive float or 'e'
        The base of the desired exponential function.

    Returns
    -------
    exp : function
        The base-`b` exponential function. The returned function will operate
        elementwise on NumPy arrays, but note, it is not a ufunc.

    Examples
    --------
    >>> exp2 = exp_func(2)
    >>> exp2(1)
    2.0
    >>> exp3 = exp_func(3)
    >>> exp3(1)
    3.0

    Raises
    ------
    InvalidBase
        If the base is less than zero or equal to one.

    """
    from dit.utils import is_string_like
    if is_string_like(b) and b not in acceptable_base_strings:
        raise InvalidBase(msg=b)
    if b == 'linear':
        exp = lambda x: x
    elif b == 2:
        exp = np.exp2
    elif b == 10:
        exp = lambda x: 10 ** x
    elif b == 'e' or np.isclose(b, np.e):
        exp = np.exp
    else:
        if b <= 0 or b == 1:
            raise InvalidBase(b)

        def exp(x, base=b):
            """
            Return `base`**`x`

            Parameters
            ----------
            x : float
                The number to exponentiate
            base : float
                The base of the exponential

            Returns
            -------
            p : float
                `base`**`x`
            """
            return base ** np.asarray(x)
    return exp