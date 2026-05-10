def save_multiple_synth(series, source, version, n_steps, discard, n_walkers=960, walkers=True, posteriors=True, contours=False, display=False, mass_radius=True, synth=True, compressed=False):
    """Save plots for multiple series in a synthetic data batch
    """
    default_plt_options()
    for ser in series:
        if synth:
            full_source = f'{source}_{ser}'
        else:
            full_source = source
        chain = mcmc_tools.load_chain(full_source, n_walkers=n_walkers, n_steps=n_steps, version=version, compressed=compressed)
        if walkers:
            plot_walkers(chain, source=full_source, save=True, display=display, version=version)
        if posteriors:
            plot_posteriors(chain, source=full_source, save=True, discard=discard, display=display, version=version)
        if contours:
            plot_contours(chain, source=full_source, save=True, discard=discard, display=display, version=version)
        if mass_radius:
            plot_mass_radius(chain, source=full_source, save=True, discard=discard, display=display, version=version)