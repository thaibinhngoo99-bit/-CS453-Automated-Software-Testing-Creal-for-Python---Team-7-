def metropolishastings_pham(logpdf, loggrad, loghess, nsamps, initstate, stepsize, nsteps, ninits):
    """
    Convenience function for preconditioned Hamiltonian MCMC.
    """
    logdens = logdensity.LogDensity(logpdf, loggrad, loghess)
    phmc = PrecondHamiltonianMC(logdens, nsteps)
    return phmc.sample_nd(nsamps, initstate, stepsize, ninits)