def get_generator_map():
    """Returns a map from the generator ID to a SequenceGenerator class creator.

  Binds the `config` argument so that the arguments match the
  BaseSequenceGenerator class constructor.

  Returns:
    Map from the generator ID to its SequenceGenerator class creator with a
    bound `config` argument.
  """

    def create_sequence_generator(config, **kwargs):
        return ImprovRnnSequenceGenerator(improv_rnn_model.ImprovRnnModel(config), config.details, steps_per_quarter=config.steps_per_quarter, **kwargs)
    return {key: partial(create_sequence_generator, config) for key, config in improv_rnn_model.default_configs.items()}