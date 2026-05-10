def diis_update(F_prev_list, r_prev_list):
    c = diis_solver(r_prev_list)
    out = 0 * F_prev_list[0]
    for i, element in enumerate(F_prev_list):
        out += c[i] * element
    return out