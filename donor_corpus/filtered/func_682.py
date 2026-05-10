def plot_gravitational_contours(chain, discard, source, version, cap=None, display=True, save=False, r_nw=10, sigmas=np.linspace(0, 2, 5), summary=False, unit_labels=True, fontsize=16, fixed_grav=False, figsize=None):
    """Plots contours of gravitational parameters
    """
    cc = mcmc_tools.setup_gravitational_chainconsumer(chain=chain, discard=discard, source=source, version=version, cap=cap, fixed_grav=fixed_grav, summary=summary, r_nw=r_nw, unit_labels=unit_labels, sigmas=sigmas, fontsize=fontsize)
    if fixed_grav:
        fig = cc.plotter.plot_distributions(figsize=figsize)
        plt.tight_layout()
    else:
        fig = cc.plotter.plot()
    save_plot(fig, prefix='gravitational', chain=chain, save=save, source=source, version=version, display=display)
    return fig