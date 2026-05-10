def train_pytorch(reader, train_data, test_data, dev_data, configuration: dict, debug=False):
    import torch
    seed = configuration.get('seed')
    random.seed(seed)
    torch.manual_seed(seed)
    clip_value = configuration.get('clip_value')
    batch_size = configuration.get('batch_size')
    epochs = configuration.get('epochs')
    l2 = configuration.get('l2')
    optimizer = configuration.get('optimizer')
    learning_rate = configuration.get('learning_rate')
    learning_rate_decay = configuration.get('learning_rate_decay')
    log_interval = configuration.get('log_interval')
    validation_interval = configuration.get('validation_interval')
    tensorboard_folder = configuration.get('tensorboard_folder')
    model = configuration.get('reader')
    save_dir = configuration.get('save_dir')
    write_metrics_to = configuration.get('write_metrics_to')
    reader.setup_from_data(train_data, is_training=True)
    if clip_value != 0.0:
        clip_value = (-abs(clip_value), abs(clip_value))
    name_to_optimizer = {'gd': torch.optim.SGD, 'adam': torch.optim.Adam, 'adagrad': torch.optim.Adagrad, 'adadelta': torch.optim.Adadelta}
    if optimizer not in name_to_optimizer:
        raise ValueError('Unknown optimizer: {}'.format(optimizer))
    torch_optimizer_class = name_to_optimizer[optimizer]
    params = list(reader.model_module.prediction_module.parameters())
    params.extend(reader.model_module.loss_module.parameters())
    torch_optimizer = torch_optimizer_class(params, lr=learning_rate)
    sw = None
    if tensorboard_folder is not None:
        if os.path.exists(tensorboard_folder):
            shutil.rmtree(tensorboard_folder)
        sw = tf.summary.FileWriter(tensorboard_folder)
    iter_interval = 1 if debug else log_interval
    hooks = [LossHook(reader, iter_interval, summary_writer=sw), ExamplesPerSecHook(reader, batch_size, iter_interval, sw)]
    preferred_metric, best_metric = readers.eval_hooks[model].preferred_metric_and_initial_score()

    def side_effect(metrics, prev_metric):
        """Returns: a state (in this case a metric) that is used as input for the next call"""
        m = metrics[preferred_metric]
        if prev_metric is not None and m < prev_metric:
            for param_group in torch_optimizer.param_groups:
                param_group['lr'] *= learning_rate_decay
                logger.info('Decayed learning rate to: %.5f' % param_group['lr'])
        elif m > best_metric[0] and save_dir is not None:
            best_metric[0] = m
            if prev_metric is None:
                reader.store(save_dir)
            else:
                reader.model_module.store(os.path.join(save_dir, 'model_module'))
            logger.info('Saving model to: %s' % save_dir)
        return m
    hooks.append(readers.eval_hooks[model](reader, dev_data, batch_size, summary_writer=sw, side_effect=side_effect, iter_interval=validation_interval, epoch_interval=1 if validation_interval is None else None, write_metrics_to=write_metrics_to))
    reader.train(torch_optimizer, train_data, batch_size, max_epochs=epochs, hooks=hooks, l2=l2, clip=clip_value)
    if dev_data is not None and save_dir is not None:
        reader.load(save_dir)
        result_dict = evaluate_reader(reader, dev_data, batch_size)
        logger.info('############### Results on the Dev Set##############')
        pretty_print_results(result_dict)
    if test_data is not None and save_dir is not None:
        reader.load(save_dir)
        result_dict = evaluate_reader(reader, test_data, batch_size)
        logger.info('############### Results on the Test Set##############')
        pretty_print_results(result_dict)