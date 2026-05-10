def diis_update_uhf(F_prev_lists, r_prev_lists):
    c = diis_solver_uhf(r_prev_lists[0], r_prev_lists[1])
    Fa = 0 * F_prev_lists[0][0]
    for i, element in enumerate(F_prev_lists[0]):
        Fa += c[i] * element
    Fb = 0 * F_prev_lists[0][0]
    for i, element in enumerate(F_prev_lists[1]):
        Fb += c[i] * element
    return (Fa, Fb)