def metropolishastings_lang(logpdf, loggrad, nsamps, initstate, pwidth, ninits):
    """
    Convenience function for Metropolis-Hastings sampling with
    Langevin dynamics proposal kernel.
    """
    logdens = logdensity.LogDensity(logpdf, loggrad)
    langmh = LangevinMH(logdens)
    return langmh.sample_nd(nsamps, initstate, pwidth, ninits)