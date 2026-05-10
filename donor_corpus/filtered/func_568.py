def analyze_episodic(model, test_data, args):
    model.eval()
    m, x_ = test_data[0]
    m = m.to(args.device)
    x = x_[:, :, :-1].to(args.device)
    y = x_[:, :, -1].type(torch.long).to(args.device)
    y = y.squeeze()
    with torch.no_grad():
        y_hat, attention = model(x, m)
        attention = attention[0]
        attention = np.squeeze(attention)
    grid = test_data.grid
    train = grid.train
    test = grid.test
    n_train = len(train)
    n_test = len(test)
    rel_ids = grid.hub_sample_ids
    attn_ranks = np.zeros_like(attention)
    for i in range(n_test):
        argsorted_attn = np.argsort(attention[i])
        ranks = np.zeros([n_train])
        ranks[argsorted_attn] = np.arange(n_train)
        attn_ranks[i] = ranks
    relevant = []
    irrelevant = []
    for i in range(n_test):
        for j in range(n_train):
            if j in rel_ids[i]:
                relevant.append(attn_ranks[i, j])
            else:
                irrelevant.append(attn_ranks[i, j])
    rank_data = {'relevant': relevant, 'irrelevant': irrelevant}
    k = 8
    used_hub = []
    for i in range(n_test):
        highest_attn = np.argsort(attention[i])[-k:]
        test_f1, test_f2, test_ctx, test_y = test[i]
        hubs = []
        for rel_id in rel_ids[i]:
            train_sample = train[rel_id]
            train_f1, train_f2 = (train_sample[0], train_sample[1])
            if train_f1 in [test_f1, test_f2]:
                hubs.append(train_f2)
            if train_f2 in [test_f1, test_f2]:
                hubs.append(train_f1)
        hubs = list(set(hubs))
        hubs_dict = {h: [] for h in hubs}
        assert len(hubs) == 2, "shouldn't be more than 2 hubs?"
        attended_train = [train[idx] for idx in highest_attn]
        for sample in attended_train:
            train_f1, train_f2, train_ctx, train_y = sample
            if train_ctx != test_ctx:
                continue
            if hubs[0] == train_f1:
                hubs_dict[hubs[0]].append(sample[1])
            if hubs[1] == sample[0]:
                hubs_dict[hubs[1]].append(sample[1])
            if hubs[0] == sample[1]:
                hubs_dict[hubs[0]].append(sample[0])
            if hubs[1] == sample[1]:
                hubs_dict[hubs[1]].append(sample[0])
        if test_f1 in hubs_dict[hubs[0]] and test_f2 in hubs_dict[hubs[0]]:
            used_hub.append(True)
        elif test_f1 in hubs_dict[hubs[1]] and test_f2 in hubs_dict[hubs[1]]:
            used_hub.append(True)
        else:
            used_hub.append(False)
    p_used_hub = np.mean(used_hub)
    print('Proportion that episodic system retrieved a hub path:', p_used_hub)
    results = {'rank_data': rank_data, 'p_used_hub': p_used_hub}
    return results