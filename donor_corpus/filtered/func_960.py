def _tensorflow_autoconf_impl(repository_ctx):
    """Implementation of tensorflow autoconf. rule."""
    tf_conf = _get_tf_conf(repository_ctx)
    print('Using %s=%s' % (_TF_INCLUDE_PATH, tf_conf.include_path))
    print('Using %s=%s' % (_TF_LIB_PATH, tf_conf.lib_path))
    repository_ctx.symlink(tf_conf.include_path, 'include')
    repository_ctx.symlink(tf_conf.lib_path, 'lib')
    repository_ctx.template('BUILD', Label('//third_party/tensorflow:tensorflow.BUILD'))