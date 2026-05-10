def _validate_session_write_concern(session, write_concern):
    """Validate that an explicit session is not used with an unack'ed write.

    Returns the session to use for the next operation.
    """
    if session:
        if write_concern is not None and (not write_concern.acknowledged):
            if session._implicit:
                return None
            else:
                raise ConfigurationError('Explicit sessions are incompatible with unacknowledged write concern: %r' % (write_concern,))
    return session