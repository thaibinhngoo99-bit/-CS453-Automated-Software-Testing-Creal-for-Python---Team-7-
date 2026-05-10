def minmaxnormalize(sub_data):
    zeros = sub_data == 0
    max = np.max(sub_data)
    min = np.min(sub_data)
    norm = (sub_data - min) / (max - min)
    norm[zeros] = 0
    return norm