def plot_epoch_posteriors(master_cc, source, version, display=True, save=False, col_wrap=None, alt_params=True, unit_labels=True, add_text=True, fontsize=16):
    """Plot posteriors for multiiple epoch chains

    parameters
    ----------
    master_cc : ChainConsumer
        Contains the multi-epoch chain, created with setup_master_chainconsumer()
    source : str
    version : int
    display : bool (optional)
    save : bool (optional)
    col_wrap : int (optional)
    """
    param_order = {'grid5': ['mdot1', 'mdot2', 'mdot3', 'qb1', 'qb2', 'qb3', 'x', 'z', 'm_nw', 'm_gr', 'd_b', 'xi_ratio'], 'he2': ['mdot1', 'mdot2', 'qb1', 'qb2', 'm_gr', 'd_b', 'xi_ratio']}
    param_keys = param_order[source]
    if alt_params:
        param_keys = ['mdot1', 'mdot2', 'mdot3', 'qb1', 'qb2', 'qb3', 'x', 'z', 'g', 'M', 'd_b', 'xi_ratio']
    formatted_params = plot_tools.convert_mcmc_labels(param_keys, unit_labels=unit_labels)
    n_epochs = len(master_cc.chains) - 1
    if col_wrap is None:
        col_wrap = n_epochs
    height = 3 * ceil(len(param_keys) / n_epochs)
    fig = master_cc.plotter.plot_distributions(parameters=formatted_params, col_wrap=col_wrap, figsize=[8, height], display=False)
    if add_text:
        add_epoch_text(fig, fontsize=fontsize)
    plt.tight_layout()
    save_plot(fig, prefix='multi_posteriors', save=save, source=source, version=version, display=display, enforce_chain_info=False)
    return fig