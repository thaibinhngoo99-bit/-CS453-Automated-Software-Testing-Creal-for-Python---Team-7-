def plot_mass_radius(chain, discard, source, version, cap=None, display=True, save=False, summary=False, sigmas=np.linspace(0, 2, 5), fontsize=18, figsize='column'):
    """Plots contours of mass versus radius from a given chain
    """
    default_plt_options()
    mass_nw, mass_gr = mcmc_params.get_constant_masses(source, version)
    mass_radius_chain = mcmc_params.get_mass_radius_chain(chain=chain, discard=discard, source=source, version=version, cap=cap, mass_nw=mass_nw, mass_gr=mass_gr)
    cc = mcmc_tools.setup_custom_chainconsumer(mass_radius_chain, parameters=['R', 'M'], sigmas=sigmas, summary=summary, fontsize=fontsize)
    fig = cc.plotter.plot(figsize=figsize)
    fig.subplots_adjust(left=0.16, bottom=0.15)
    save_plot(fig, prefix='mass-radius', chain=chain, save=save, source=source, version=version, display=display)
    return fig