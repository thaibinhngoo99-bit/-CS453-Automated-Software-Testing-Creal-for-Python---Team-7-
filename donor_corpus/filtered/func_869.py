def general_adaptive_loss(x, shape, bowl=1.0):
    input_shape = x.shape
    shape = torch.as_tensor(shape).to(x.device)
    bowl = torch.as_tensor(bowl).to(x.device)
    b = x.size(0)
    x = x.view(b, -1)
    if len(shape.shape) == 0:
        shape = shape.unsqueeze(dim=0).expand([b]).unsqueeze(dim=1)
    else:
        shape = shape.view(b, -1)
    if len(bowl.shape) == 0:
        bowl = bowl.unsqueeze(dim=0).expand([b]).unsqueeze(dim=1)
    else:
        bowl = bowl.view(b, -1)
    partition = get_partition(shape)
    ans = torch.abs(shape - 2) / shape * (torch.pow(torch.square(x / bowl) / torch.abs(shape - 2) + 1, shape / 2) - 1) + log_safe(bowl) + log_safe(partition)
    return ans.view(input_shape)