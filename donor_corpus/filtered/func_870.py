def entropy(x):
    """Calculate entropy of a pre-softmax logit Tensor"""
    exp_x = torch.exp(x)
    A = torch.sum(exp_x, dim=1)
    B = torch.sum(x * exp_x, dim=1)
    return torch.log(A) - B / A