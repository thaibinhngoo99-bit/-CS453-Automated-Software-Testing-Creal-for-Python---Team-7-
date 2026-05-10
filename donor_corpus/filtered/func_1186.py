def metropolishastings_plang(logpdf, loggrad, loghess, nsamps, initstate, pwidth, ninits):
    """
    Convenience function for Metropolis-Hastings sampling with
    Riemannian (preconditioned) Langevin dynamics proposal kernel.
    """
    logdens = logdensity.LogDensity(logpdf, loggrad, loghess)
    plangmh = PrecondLangevinMH(logdens)
    return plangmh.sample_nd(nsamps, initstate, pwidth, ninits)