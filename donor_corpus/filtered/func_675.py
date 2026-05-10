def save_plot(fig, prefix, save, source, version, display, chain=None, n_dimensions=None, n_walkers=None, n_steps=None, label=None, extension='.png', enforce_chain_info=True):
    """Handles saving/displaying of a figure passed to it
    """
    if enforce_chain_info and None in (n_dimensions, n_walkers, n_steps):
        if chain is None:
            raise ValueError('Must provide chain, or specify each of (n_dimensions, n_walkers, n_steps)')
        else:
            n_walkers, n_steps, n_dimensions = chain.shape
    if save:
        filename = mcmc_tools.get_mcmc_string(source=source, version=version, n_walkers=n_walkers, n_steps=n_steps, prefix=prefix, label=label, extension=extension)
        source_path = get_source_path(source)
        filepath = os.path.join(source_path, 'plots', prefix, f'{filename}')
        fig.savefig(filepath)
    if display:
        plt.show(block=False)
    else:
        plt.close(fig)