def log_func(b):
    """
    Returns a base-`b` logarithm function.

    Parameters
    ----------
    b : positive float or 'e'
        The base of the desired logarithm function.

    Returns
    -------
    log : function
        The base-`b` logarithm function. The returned function will operate
        elementwise on NumPy arrays, but note, it is not a ufunc.

    Examples
    --------
    >>> log2 = log_func(2)
    >>> log2(2)
    1.0
    >>> log3 = log_func(3)
    >>> log3(3)
    1.0

    Raises
    ------
    InvalidBase
        If the base is less than zero or equal to one.

    """
    from dit.utils import is_string_like
    if is_string_like(b) and b not in acceptable_base_strings:
        raise InvalidBase(msg=b)
    if b == 'linear':
        log = lambda x: x
    elif b == 2:
        log = np.log2
    elif b == 10:
        log = np.log10
    elif b == 'e' or np.isclose(b, np.e):
        log = np.log
    else:
        if b <= 0 or b == 1:
            raise InvalidBase(b)
        Z = np.log(b)

        def log(x, func=np.log):
            """
            Return the log of `x`

            Parameters
            ----------
            x : float
                The value to take the log of
            func : function
                A logarithm function

            Returns
            -------
            log : float
                The logarithm of `x` in base `b` (from outer scope)
            """
            return func(x) / Z
    return log