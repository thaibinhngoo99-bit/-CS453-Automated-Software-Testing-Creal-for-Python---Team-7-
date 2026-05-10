def default_plt_options():
    """Initialise default plot parameters"""
    params = {'mathtext.default': 'regular', 'font.family': 'serif', 'text.usetex': False}
    plt.rcParams.update(params)