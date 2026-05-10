def get_icicicc_csv(data_row):
    """Convert a transaction row to tuple.

    Details of fields
        0: 'D',     # Transaction date
        2: 'M',     # Transaction details
        5: 'T',     # Amount
    """
    logger.debug('get_icicicsv: Data row = {}'.format(data_row))
    date = data_row[0]
    if _valid_date(date, date_format='%d/%m/%Y'):
        amt = '-{}'.format(data_row[5])
        if data_row[6] == 'CR':
            amt = data_row[5]
        return Transaction(id=0, date=date, payee='', memo=data_row[2], amount=amt)
    return InvalidTransaction()