def metropolishastings_ham(logpdf, loggrad, nsamps, initstate, stepsize, nsteps, ninits):
    """
    Convenience function for Hamiltonian MCMC.
    """
    logdens = logdensity.LogDensity(logpdf, loggrad)
    hmc = HamiltonianMC(logdens, nsteps)
    return hmc.sample_nd(nsamps, initstate, stepsize, ninits)