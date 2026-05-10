def plot_contours(chain, discard, source, version, cap=None, display=True, save=False, truth_values=None, parameters=None, sigmas=np.linspace(0, 2, 5), cc=None, summary=False, fontsize=14, max_ticks=4):
    """Plots posterior contours of mcmc chain

    parameters : [str]
        specify which parameters to plot
    """
    default_plt_options()
    if cc is None:
        pkeys = mcmc_versions.get_parameter(source, version, 'param_keys')
        pkey_labels = plot_tools.convert_mcmc_labels(param_keys=pkeys)
        cc = mcmc_tools.setup_chainconsumer(chain=chain, param_labels=pkey_labels, discard=discard, cap=cap, sigmas=sigmas, summary=summary, fontsize=fontsize, max_ticks=max_ticks)
    if parameters is not None:
        parameters = plot_tools.convert_mcmc_labels(param_keys=parameters)
    if truth_values is not None:
        fig = cc.plotter.plot(truth=truth_values, parameters=parameters)
    else:
        fig = cc.plotter.plot(parameters=parameters)
    save_plot(fig, prefix='contours', chain=chain, save=save, source=source, version=version, display=display)
    return fig