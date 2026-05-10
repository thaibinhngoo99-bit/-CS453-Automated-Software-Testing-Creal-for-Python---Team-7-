def plot_autocorrelation(chain, source, version, n_points=10, load=True, save_tau=True, ylims=None):
    """Plots estimated integrated autocorrelation time

        Note: Adapted from https://dfm.io/posts/autocorr/
    """
    mv = mcmc_versions.McmcVersion(source=source, version=version)
    params_fmt = plot_tools.convert_mcmc_labels(mv.param_keys)
    if load:
        sample_steps, autoc = mcmc_tools.load_autocorrelation(source, version=version, n_steps=chain.shape[1])
    else:
        sample_steps, autoc = mcmc_tools.get_autocorrelation(chain, source=source, version=version, n_points=n_points, save=save_tau)
    fig, ax = plt.subplots()
    for i, param in enumerate(mv.param_keys):
        ax.loglog(sample_steps, autoc[i], 'o-', label=f'{params_fmt[i]}')
    ax.plot(sample_steps, sample_steps / 10.0, '--k', label='$\\tau = N/10$')
    if ylims is None:
        xlim = ax.get_xlim()
        ylims = [5, xlim[1] / 10]
    ax.set_ylim(ylims)
    ax.set_xlabel('N steps')
    ax.set_ylabel('$\\tau$ estimate (N)')
    ax.legend(fontsize=14, ncol=2, labelspacing=0.3)
    plt.show(block=False)
    return fig