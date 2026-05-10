def plot_distance_anisotropy(chain, discard, source, version, cap=None, display=True, save=False, sigmas=np.linspace(0, 2, 5), summary=False, figsize=(4, 4), unit_labels=True, fontsize=18):
    """Plots contours of MCMC parameters d_b, xi_ratio
    """
    d_b_chain = mcmc_params.get_param_chain(chain, param='d_b', discard=discard, source=source, version=version, cap=cap)
    xi_ratio_chain = mcmc_params.get_param_chain(chain, param='xi_ratio', discard=discard, source=source, version=version, cap=cap)
    flat_chain = np.column_stack([d_b_chain, xi_ratio_chain])
    cc = mcmc_tools.setup_custom_chainconsumer(flat_chain, parameters=['d_b', 'xi_ratio'], sigmas=sigmas, summary=summary, unit_labels=unit_labels, fontsize=fontsize)
    fig = cc.plotter.plot(figsize=figsize)
    fig.subplots_adjust(left=0.2, bottom=0.2)
    save_plot(fig, prefix='distance', chain=chain, save=save, source=source, version=version, display=display)
    return fig