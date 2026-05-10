def name2tensor(name):
    tensor = torch.zeros(len(name), 1, dict_size)
    for i, char in enumerate(name):
        tensor[i, 0, char2index(char)] = 1
    return tensor