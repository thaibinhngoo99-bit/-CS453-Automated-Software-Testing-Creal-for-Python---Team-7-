def _reraise_with_unknown_commit(exc):
    """Re-raise an exception with the UnknownTransactionCommitResult label."""
    exc._add_error_label('UnknownTransactionCommitResult')
    reraise_instance(exc, trace=sys.exc_info()[2])