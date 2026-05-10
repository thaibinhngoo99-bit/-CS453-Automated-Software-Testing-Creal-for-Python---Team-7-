def clip_grad_norm_(params, max_norm, aggregate_norm_fn=None) -> torch.Tensor:
    if isinstance(params, torch.Tensor):
        params = [params]
    params = list(params)
    grads = [p.grad.detach() for p in filter(lambda p: p.grad is not None, params)]
    if len(grads) == 0:
        if len(params) > 0:
            return params[0].new_tensor(0.0)
        else:
            return torch.tensor(0.0)
    if len(grads) == 1:
        total_norm = torch.norm(grads[0], p=2, dtype=torch.float32)
    elif multi_tensor_l2norm_available:
        total_norm = multi_tensor_total_norm(grads)
    else:
        warnings.warn("amp_C fused kernels unavailable, disabling multi_tensor_l2norm; you may get better performance by installing NVIDIA's apex library")
        total_norm = torch.norm(torch.stack([torch.norm(g, p=2, dtype=torch.float32) for g in grads]))
    if aggregate_norm_fn is not None:
        total_norm = aggregate_norm_fn(total_norm)
    if max_norm > 0:
        max_norm = float(max_norm)
        clip_coef = (max_norm / (total_norm + 1e-06)).clamp_(max=1)
        for g in grads:
            g.mul_(clip_coef)
    return total_norm