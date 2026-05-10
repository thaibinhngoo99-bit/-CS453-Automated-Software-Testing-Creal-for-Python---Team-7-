def plot_qb_mdot(chain, source, version, discard, cap=None, display=True, save=False, figsize=(5, 5), fontsize=16, sigmas=(1, 2)):
    """Plots 2D contours of Qb versus Mdot for each epoch (from multi-epoch chain)
    """
    mv = mcmc_versions.McmcVersion(source=source, version=version)
    chain_flat = mcmc_tools.slice_chain(chain, discard=discard, cap=cap, flatten=True)
    system_table = obs_tools.load_summary(mv.system)
    epochs = list(system_table.epoch)
    cc = chainconsumer.ChainConsumer()
    param_labels = []
    for param in ['mdot', 'qb']:
        param_labels += [plot_tools.full_label(param)]
    for i, epoch in enumerate(epochs):
        mdot_idx = mv.param_keys.index(f'mdot{i + 1}')
        qb_idx = mv.param_keys.index(f'qb{i + 1}')
        param_idxs = [mdot_idx, qb_idx]
        cc.add_chain(chain_flat[:, param_idxs], parameters=param_labels, name=str(epoch))
    cc.configure(kde=False, smooth=0, label_font_size=fontsize, tick_font_size=fontsize - 2, sigmas=sigmas)
    fig = cc.plotter.plot(display=False, figsize=figsize)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    save_plot(fig, prefix='qb', save=save, source=source, version=version, display=display, chain=chain)
    return fig