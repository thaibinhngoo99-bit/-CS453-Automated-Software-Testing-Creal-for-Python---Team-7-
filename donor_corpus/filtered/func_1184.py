def metropolishastings_rw(logpdf, nsamps, initstate, pwidth, ninits):
    """
    Convenience function for Metropolis-Hastings sampling with
    random walk proposal kernel.
    """
    logdens = logdensity.LogDensity(logpdf)
    rwmh = RandomWalkMH(logdens)
    return rwmh.sample_nd(nsamps, initstate, pwidth, ninits)