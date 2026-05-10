def plot_inclination(chain, discard, source, version, cap=None, display=True, save=False, disc_model='he16_a', sigmas=np.linspace(0, 2, 5), summary=False, unit_labels=True, figsize=(4, 4), fontsize=18):
    """Plots contours of parameters derived using disc model
    """
    disc_chain = mcmc_params.get_disc_chain(chain=chain, discard=discard, cap=cap, source=source, version=version, disc_model=disc_model)
    cc = mcmc_tools.setup_custom_chainconsumer(disc_chain, parameters=['d', 'i'], sigmas=sigmas, summary=summary, unit_labels=unit_labels, fontsize=fontsize)
    fig = cc.plotter.plot(figsize=figsize)
    fig.subplots_adjust(left=0.15, bottom=0.15)
    save_plot(fig, prefix='disc', chain=chain, save=save, source=source, version=version, display=display)
    return fig