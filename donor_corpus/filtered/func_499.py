def sampler(labels: torch.Tensor, nbins: int=10, stratify: bool=False) -> WeightedRandomSampler:
    discretize = pd.qcut if stratify else pd.cut
    bin_labels = torch.LongTensor(discretize(labels.tolist(), nbins, labels=False, duplicates='drop'))
    class_sample_count = torch.LongTensor([(bin_labels == t).sum() for t in torch.arange(nbins)])
    weight = 1.0 / class_sample_count.float()
    sample_weights = torch.zeros_like(labels)
    for t in torch.unique(bin_labels):
        sample_weights[bin_labels == t] = weight[t]
    return WeightedRandomSampler(sample_weights, len(sample_weights))