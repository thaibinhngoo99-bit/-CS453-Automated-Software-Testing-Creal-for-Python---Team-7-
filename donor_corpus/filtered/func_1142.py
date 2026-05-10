def maximum_likelihood_estimate_sgd(distr_output: DistributionOutput, samples: mx.ndarray, init_biases: List[mx.ndarray.NDArray]=None, num_epochs: PositiveInt=PositiveInt(5), learning_rate: PositiveFloat=PositiveFloat(0.01), hybridize: bool=True) -> Iterable[float]:
    model_ctx = mx.cpu()
    arg_proj = distr_output.get_args_proj()
    arg_proj.initialize()
    if hybridize:
        arg_proj.hybridize()
    if init_biases is not None:
        for param, bias in zip(arg_proj.proj, init_biases):
            param.params[param.prefix + 'bias'].initialize(mx.initializer.Constant(bias), force_reinit=True)
    trainer = mx.gluon.Trainer(arg_proj.collect_params(), 'sgd', {'learning_rate': learning_rate, 'clip_gradient': 10.0})
    dummy_data = mx.nd.array(np.ones((len(samples), 1)))
    train_data = mx.gluon.data.DataLoader(mx.gluon.data.ArrayDataset(dummy_data, samples), batch_size=BATCH_SIZE, shuffle=True)
    for e in range(num_epochs):
        cumulative_loss = 0
        num_batches = 0
        for i, (data, sample_label) in enumerate(train_data):
            data = data.as_in_context(model_ctx)
            sample_label = sample_label.as_in_context(model_ctx)
            with mx.autograd.record():
                distr_args = arg_proj(data)
                distr = distr_output.distribution(distr_args)
                loss = distr.loss(sample_label)
                if not hybridize:
                    assert loss.shape == distr.batch_shape
            loss.backward()
            trainer.step(BATCH_SIZE)
            num_batches += 1
            cumulative_loss += mx.nd.mean(loss).asscalar()
        print('Epoch %s, loss: %s' % (e, cumulative_loss / num_batches))
    return [param[0].asnumpy() for param in arg_proj(mx.nd.array(np.ones((1, 1))))]