def compile_scheduler_options(scheduler_options, search_strategy, search_options, nthreads_per_trial, ngpus_per_trial, checkpoint, num_trials, time_out, resume, visualizer, time_attr, reward_attr, dist_ip_addrs, epochs=None):
    """
    Updates a copy of scheduler_options (scheduler-specific options, can be
    empty) with general options. The result can be passed to __init__ of the
    scheduler.

    Special role of epochs for HyperbandScheduler: If the search_strategy
    involves HyperbandScheduler and epochs is given, then this value is
    copied to scheduler_options['max_t']. Pass epochs for applications
    where the time_attr is epoch, and epochs is the maximum number of
    epochs.

    :param scheduler_options:
    :param search_strategy:
    :param search_options:
    :param nthreads_per_trial:
    :param ngpus_per_trial:
    :param checkpoint:
    :param num_trials:
    :param time_out:
    :param resume:
    :param visualizer:
    :param time_attr:
    :param reward_attr:
    :param dist_ip_addrs:
    :param kwargs:
    :param epochs: See above. Optional
    :return: Copy of scheduler_options with updates

    """
    if scheduler_options is None:
        scheduler_options = dict()
    else:
        assert isinstance(scheduler_options, dict)
    assert isinstance(search_strategy, str)
    if search_options is None:
        search_options = dict()
    if visualizer is None:
        visualizer = 'none'
    if time_attr is None:
        time_attr = 'epoch'
    if reward_attr is None:
        reward_attr = 'accuracy'
    scheduler_options = copy.copy(scheduler_options)
    scheduler_options.update({'resource': {'num_cpus': nthreads_per_trial, 'num_gpus': ngpus_per_trial}, 'searcher': search_strategy, 'search_options': search_options, 'checkpoint': checkpoint, 'resume': resume, 'num_trials': num_trials, 'time_out': time_out, 'reward_attr': reward_attr, 'time_attr': time_attr, 'visualizer': visualizer, 'dist_ip_addrs': dist_ip_addrs})
    searcher = searcher_for_hyperband_strategy.get(search_strategy)
    if searcher is not None:
        scheduler_options['searcher'] = searcher
        if epochs is not None:
            scheduler_options['max_t'] = epochs
    return scheduler_options