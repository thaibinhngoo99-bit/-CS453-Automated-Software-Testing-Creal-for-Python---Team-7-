def sub_graph(adj, num):
    """
    Monte carlo sample a number of neighbors for each node given the adjacent matrix
    adj: normalized and processed graph adjacent matrix
    num: the number of samples for each neighbor
    """
    nodes = adj.shape[0]
    neighbor_number = torch.sum(adj > 0, dim=1).reshape(node, 1) / num
    sub_graph = torch.randint(0, nodes, (nodes, num))
    sub_graph = sub_graph.reshape(-1).cpu().tolist()
    sub_graph = list(set(sub_graph))
    mask = torch.zeros(nodes, nodes)
    mask[sub_graph, sub_graph] = 1
    return adj * mask * neighbor_number