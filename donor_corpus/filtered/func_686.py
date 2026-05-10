def plot_walkers(chain, source, version, params=None, n_lines=30, xlim=-1, display=True, save=False, label=''):
    """Plots walkers vs steps (i.e. "time")

    Parameters
    ----------
    source : str
    version : int
    chain : np.array
        chain as returned by load_chain()
    params : [str]
        parameter(s) of which to plot walkers.
    n_lines : int
        approx number of lines/walkers to plot on parameter
    xlim : int
        x-axis limit to plot (n_steps), i.e. ax.set_xlim((0, xlim))
    label : str
        optional label to add to filename when saving
    display : bool
    save : bool
    """
    default_plt_options()
    pkeys = mcmc_versions.get_parameter(source, version, 'param_keys')
    if params is None:
        half = int(len(pkeys) / 2)
        for i, param_split in enumerate((pkeys[:half], pkeys[half:])):
            plot_walkers(chain=chain, source=source, version=version, params=param_split, n_lines=n_lines, xlim=xlim, display=display, save=save, label=f'P{i + 1}')
        return
    n_walkers, n_steps, n_dim = chain.shape
    n_params = len(params)
    jump_size = round(n_walkers / n_lines)
    steps = np.arange(n_steps)
    walker_idxs = np.arange(0, n_walkers, jump_size)
    fig, ax = plt.subplots(n_params, 1, sharex=True, figsize=(10, 12))
    for i in range(n_params):
        p_idx = pkeys.index(params[i])
        for j in walker_idxs:
            walker = chain[j, :, p_idx]
            ax[i].plot(steps, walker, linewidth=0.5, color='black')
            ax[i].set_ylabel(params[i])
    if xlim == -1:
        xlim = n_steps
    ax[-1].set_xlabel('Step')
    ax[-1].set_xlim([0, xlim])
    plt.tight_layout()
    if display:
        plt.show(block=False)
    save_plot(fig, prefix='walkers', chain=chain, save=save, source=source, version=version, display=display, label=label, extension='.png')