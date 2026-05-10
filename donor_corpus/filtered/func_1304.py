def get_importation_rate_func_as_birth_rates(importation_times: List[float], importation_n_cases: List[float], detect_prop_func, starting_pops: list):
    """
    When imported cases are explicitly simulated as part of the modelled population. They enter the late_infectious
    compartment through a birth process
    """
    for i, time in enumerate(importation_times):
        importation_n_cases[i] /= detect_prop_func(time)
    importation_numbers_scale_up = scale_up_function(importation_times, importation_n_cases, method=4, smoothness=5.0, bound_low=0.0)

    def recruitment_rate(t):
        return importation_numbers_scale_up(t) / sum(starting_pops)
    return recruitment_rate