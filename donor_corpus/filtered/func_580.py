def run_regression(x, y, grid_dist):
    stats_model = sm.OLS(y, x).fit()
    y_hat_E = stats_model.params[0] + stats_model.params[1] * grid_dist
    p_val, t_val, param, bse = (stats_model.pvalues, stats_model.tvalues, stats_model.params, stats_model.bse)
    return (y_hat_E, p_val, t_val, param, bse)