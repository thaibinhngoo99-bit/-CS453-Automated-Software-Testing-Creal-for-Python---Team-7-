def demo_ddp_hook(rank, world_size, weight, dp, noise_multiplier, max_grad_norm):
    torch.manual_seed(rank)
    batch_size = 32
    withdp = 'with' + ('out ' if not dp else '')
    print(f'Running DDP hook {withdp} differential privacy example on rank {rank}.')
    device = setup_and_get_device(rank, world_size, nonce=1)
    model = ToyModel().to(device)
    model.net1.bias.requires_grad = False
    model.net2.bias.requires_grad = False
    model.net2.weight.requires_grad = False
    ddp_model = DDP(model, device_ids=[device])
    if dp:
        engine = PrivacyEngine(ddp_model, batch_size=batch_size, sample_size=10 * batch_size, alphas=PRIVACY_ALPHAS, noise_multiplier=noise_multiplier, max_grad_norm=[max_grad_norm])
        engine.random_number_generator = engine._set_seed(0)
    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=1)
    if dp:
        engine.attach(optimizer)
    optimizer.zero_grad()
    labels = torch.randn(batch_size, 5).to(device)
    outputs = ddp_model(torch.randn(batch_size, 10).to(device))
    loss_fn(outputs, labels).backward()
    optimizer.step()
    weight.copy_(model.net1.weight.data.cpu())
    del ddp_model
    cleanup()