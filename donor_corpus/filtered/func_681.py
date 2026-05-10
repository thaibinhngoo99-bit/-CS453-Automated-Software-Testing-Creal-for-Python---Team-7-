def plot_redshift(chain, discard, source, version, cap=None, display=True, save=False):
    """Plots posterior distribution of redshift given a chain
    """
    mass_nw, mass_gr = mcmc_params.get_constant_masses(source, version)
    redshift_chain = mcmc_params.get_redshift_chain(chain=chain, discard=discard, source=source, version=version, cap=cap, mass_nw=mass_nw, mass_gr=mass_gr)
    cc = mcmc_tools.setup_custom_chainconsumer(redshift_chain, parameters=['1+z'])
    fig = cc.plotter.plot_distributions(figsize=[5, 5])
    plt.tight_layout()
    save_plot(fig, prefix='redshift', chain=chain, save=save, source=source, version=version, display=display)
    return fig