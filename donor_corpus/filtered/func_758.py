def load_ensemble_for_inference(filenames, task, model_arg_overrides=None):
    from fairseq import checkpoint_utils
    deprecation_warning('utils.load_ensemble_for_inference is deprecated. Please use checkpoint_utils.load_model_ensemble instead.')
    return checkpoint_utils.load_model_ensemble(filenames, arg_overrides=model_arg_overrides, task=task)