def __virtual__():
    """
    Only load if boto_kinesis is available.
    """
    ret = 'boto_kinesis' if 'boto_kinesis.exists' in __salt__ else False
    return ret