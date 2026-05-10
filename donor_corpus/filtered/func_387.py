def ranking(R):
    """ Produces a linear ranking of the values in R. """
    l = sorted(list(enumerate(R)), cmp=lambda a, b: cmp(a[1], b[1]))
    l = sorted(list(enumerate(l)), cmp=lambda a, b: cmp(a[1], b[1]))
    return array(map(lambda kv: kv[0], l))