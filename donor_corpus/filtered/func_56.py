def test(net, device, config, phase='val'):
    is_minknet = isinstance(net, ME.MinkowskiNetwork)
    data_loader = make_data_loader('test', is_minknet, config=config)
    net.eval()
    labels, preds = ([], [])
    with torch.no_grad():
        for batch in data_loader:
            input = create_input_batch(batch, is_minknet, device=device, quantization_size=config.voxel_size)
            logit = net(input)
            pred = torch.argmax(logit, 1)
            labels.append(batch['labels'].cpu().numpy())
            preds.append(pred.cpu().numpy())
            torch.cuda.empty_cache()
    return metrics.accuracy_score(np.concatenate(labels), np.concatenate(preds))