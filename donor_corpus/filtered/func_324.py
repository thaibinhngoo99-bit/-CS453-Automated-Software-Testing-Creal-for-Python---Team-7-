def meannormalize(sub_data):
    mean = np.mean(sub_data)
    std = np.std(sub_data)
    norm = (sub_data - mean) / std
    return (norm, mean, std)