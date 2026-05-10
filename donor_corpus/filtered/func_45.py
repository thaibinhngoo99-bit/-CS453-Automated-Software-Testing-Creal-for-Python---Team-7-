def inv_softmax(x, C=-50):
    result = torch.log(x)
    result = torch.where(result <= float('-inf'), torch.full_like(result, C), result)
    return result