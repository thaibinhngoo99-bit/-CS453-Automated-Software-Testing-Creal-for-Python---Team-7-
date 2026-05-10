def plot_max_lhood(source, version, n_walkers, n_steps, verbose=True, re_interp=False, display=True, save=False):
    default_plt_options()
    max_params, max_lhood = mcmc_tools.get_max_lhood_params(source, version=version, n_walkers=n_walkers, n_steps=n_steps, verbose=verbose, return_lhood=True)
    bfit = burstfit.BurstFit(source=source, version=version, verbose=False, re_interp=re_interp)
    lhood, fig = bfit.lhood(max_params, plot=True)
    if lhood != max_lhood:
        print_warning(f'lhoods do not match (original={max_lhood:.2f}, current={lhood:.2f}). ' + 'BurstFit (e.g. lhood, lnhood) or interpolator may have changed')
    save_plot(fig, prefix='compare', n_dimensions=len(max_params), n_walkers=n_walkers, n_steps=n_steps, save=save, source=source, version=version, display=display)