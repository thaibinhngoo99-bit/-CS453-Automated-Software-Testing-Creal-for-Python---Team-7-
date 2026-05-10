def generate_random_params(params):
    chosen_params = {}
    for param in params:
        chosen_params[param] = choice(params[param])
    return chosen_params