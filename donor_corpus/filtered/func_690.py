def plot_bprop_sample(bp_sample, source, version, bprops=None, legend=True, subplot_figsize=(3, 2.5), bfit=None, fontsize=14, vlines=True):
    """Plot burst properties from large sample against observations

    bprop_sample : np.array
        obtained using mcmc_tools.bprop_sample()
    """
    if bfit is None:
        bfit = burstfit.BurstFit(source=source, version=version, verbose=False)
    if bprops is None:
        bprops = bfit.mcmc_version.bprops
    cc = mcmc_tools.setup_bprop_chainconsumer(chain=None, n=None, discard=None, source=source, version=version, bp_sample=bp_sample)
    bp_summary = mcmc_tools.extract_bprop_summary(cc, source=source, version=version)
    n_bprops = len(bprops)
    n_rows = int(np.ceil(n_bprops / 2))
    n_cols = {False: 1, True: 2}.get(n_bprops > 1)
    figsize = (n_cols * subplot_figsize[0], n_rows * subplot_figsize[1])
    fig, ax = plt.subplots(n_rows, n_cols, sharex=False, figsize=figsize)
    if n_bprops % 2 == 1 and n_bprops > 1:
        ax[-1, -1].axis('off')
    for i, bprop in enumerate(bprops):
        subplot_row = int(np.floor(i / 2))
        subplot_col = i % 2
        if n_cols > 1:
            axis = ax[subplot_row, subplot_col]
        else:
            axis = ax
        u_model = np.diff(bp_summary[:, :, i], axis=0)
        bfit.plot_compare(model=bp_summary[1, :, i], u_model=u_model, bprop=bprop, fontsize=fontsize, ax=axis, display=False, vlines=vlines, legend=True if i == 0 and legend else False, xlabel=True if i in [n_bprops - 1] else False)
    fig.subplots_adjust(wspace=0.4)
    plt.show(block=False)
    return fig