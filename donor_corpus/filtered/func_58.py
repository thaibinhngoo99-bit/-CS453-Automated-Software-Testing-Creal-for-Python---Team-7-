def train(net, device, config):
    is_minknet = isinstance(net, ME.MinkowskiNetwork)
    optimizer = optim.SGD(net.parameters(), lr=config.lr, momentum=0.9, weight_decay=config.weight_decay)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=config.max_steps)
    print(optimizer)
    print(scheduler)
    train_iter = iter(make_data_loader('train', is_minknet, config))
    best_metric = 0
    net.train()
    for i in range(config.max_steps):
        optimizer.zero_grad()
        try:
            data_dict = train_iter.next()
        except StopIteration:
            train_iter = iter(make_data_loader('train', is_minknet, config))
            data_dict = train_iter.next()
        input = create_input_batch(data_dict, is_minknet, device=device, quantization_size=config.voxel_size)
        logit = net(input)
        loss = criterion(logit, data_dict['labels'].to(device))
        loss.backward()
        optimizer.step()
        scheduler.step()
        torch.cuda.empty_cache()
        if i % config.stat_freq == 0:
            print(f'Iter: {i}, Loss: {loss.item():.3e}')
        if i % config.val_freq == 0 and i > 0:
            torch.save({'state_dict': net.state_dict(), 'optimizer': optimizer.state_dict(), 'scheduler': scheduler.state_dict(), 'curr_iter': i}, config.weights)
            accuracy = test(net, device, config, phase='val')
            if best_metric < accuracy:
                best_metric = accuracy
            print(f'Validation accuracy: {accuracy}. Best accuracy: {best_metric}')
            net.train()