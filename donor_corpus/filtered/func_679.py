def plot_posteriors(chain, discard, source, version, cap=None, display=True, save=False, truth_values=None, cc=None):
    """Plots posterior distributions of mcmc chain

    truth_values : list|dict
        Specify parameters of point (e.g. the true value) to draw on the distributions.
    """
    default_plt_options()
    pkeys = mcmc_versions.get_parameter(source, version, 'param_keys')
    pkey_labels = plot_tools.convert_mcmc_labels(param_keys=pkeys)
    if cc is None:
        cc = mcmc_tools.setup_chainconsumer(chain=chain, param_labels=pkey_labels, discard=discard, cap=cap)
    height = 3 * ceil(len(pkeys) / 4)
    if truth_values is not None:
        fig = cc.plotter.plot_distributions(figsize=[10, height], truth=truth_values)
    else:
        fig = cc.plotter.plot_distributions(figsize=[10, height])
    plt.tight_layout()
    save_plot(fig, prefix='posteriors', chain=chain, save=save, source=source, version=version, display=display)
    return fig