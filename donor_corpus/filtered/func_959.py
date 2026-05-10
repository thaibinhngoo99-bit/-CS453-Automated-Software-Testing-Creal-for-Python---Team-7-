def _get_tf_conf(repository_ctx):
    """Returns structure containing all required information about tensorflow
     configuration on host platform.
  """
    include_path = _get_env_var_with_default(repository_ctx, _TF_INCLUDE_PATH)
    lib_path = _get_env_var_with_default(repository_ctx, _TF_LIB_PATH)
    return struct(include_path=include_path, lib_path=lib_path)