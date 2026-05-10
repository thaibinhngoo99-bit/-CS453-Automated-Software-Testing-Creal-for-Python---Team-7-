def save_all_plots(source, version, discard, n_steps, n_walkers=1000, display=False, save=True, cap=None, posteriors=True, contours=True, redshift=True, mass_radius=True, verbose=True, compressed=False):
    """Saves (and/or displays) main MCMC plots
    """
    chain = mcmc_tools.load_chain(source, version=version, n_steps=n_steps, n_walkers=n_walkers, verbose=verbose, compressed=compressed)
    if posteriors:
        printv('Plotting posteriors', verbose=verbose)
        plot_posteriors(chain, source=source, save=save, discard=discard, cap=cap, display=display, version=version)
    if contours:
        printv('Plotting contours', verbose=verbose)
        plot_contours(chain, source=source, save=save, discard=discard, cap=cap, display=display, version=version)
    if mass_radius:
        printv('Plotting mass-radius', verbose=verbose)
        plot_mass_radius(chain, source=source, save=save, discard=discard, cap=cap, display=display, version=version)
    if redshift:
        printv('Plotting redshift', verbose=verbose)
        plot_redshift(chain, source=source, save=save, discard=discard, cap=cap, display=display, version=version)