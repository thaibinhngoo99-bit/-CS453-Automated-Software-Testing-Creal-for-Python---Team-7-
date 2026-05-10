def plot_xedd(chain, discard, source, version, cap=None, display=True, save=False, cloud=True, sigmas=np.linspace(0, 2, 10), figsize=(5, 5)):
    """Plots posterior for Eddington hydrogen composition (X_Edd)
    """
    default_plt_options()
    xedd_chain = mcmc_params.get_xedd_chain(chain=chain, discard=discard, source=source, version=version, cap=cap)
    label = plot_tools.quantity_label('xedd')
    cc = mcmc_tools.setup_custom_chainconsumer(xedd_chain, parameters=[label], sigmas=sigmas, cloud=cloud)
    fig = cc.plotter.plot(figsize=figsize)
    save_plot(fig, prefix='xedd', chain=chain, save=save, source=source, version=version, display=display)
    return fig