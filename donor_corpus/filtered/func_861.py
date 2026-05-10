def add_remove_ddp_hooks(rank, world_size, remaining_hooks, dp, noise_multiplier=0, max_grad_norm=100000000.0):
    device = setup_and_get_device(rank, world_size, nonce=2)
    model = ToyModel().to(device)
    ddp_model = nn.parallel.DistributedDataParallel(model, device_ids=[device])
    engine = PrivacyEngine(ddp_model, batch_size=1, sample_size=10, alphas=PRIVACY_ALPHAS, noise_multiplier=noise_multiplier, max_grad_norm=[max_grad_norm])
    optimizer = optim.SGD(ddp_model.parameters(), lr=1)
    engine.attach(optimizer)
    remaining_hooks['attached'] = {p: p._backward_hooks for p in engine.module.parameters() if p._backward_hooks}
    engine.detach()
    remaining_hooks['detached'] = {p: p._backward_hooks for p in engine.module.parameters() if p._backward_hooks}
    cleanup()