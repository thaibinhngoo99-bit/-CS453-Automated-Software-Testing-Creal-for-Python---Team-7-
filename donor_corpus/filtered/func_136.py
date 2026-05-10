def get_SCF_err(S, D, F):
    err_v = S @ D @ F - F @ D @ S
    err = np.mean(err_v ** 2) ** 0.5
    return (err, err_v)