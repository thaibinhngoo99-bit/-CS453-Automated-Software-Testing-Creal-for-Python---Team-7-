def to_qif(transaction):
    """Transform a cleaned up row to qif format.

    Returns:
        string of a particular transaction in qif format

    See wikipedia for more details of QIF format.
    https://en.wikipedia.org/wiki/Quicken_Interchange_Format#Detail_items

    """
    logger.debug('to_qif: Input = {}'.format(transaction))
    return 'D{0}\nM{1}\nT{2}\n^\n\n'.format(transaction.date, transaction.memo, transaction.amount)