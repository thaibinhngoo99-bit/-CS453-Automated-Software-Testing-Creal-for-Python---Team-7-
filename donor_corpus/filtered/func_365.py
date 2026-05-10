def get_icici_csv(data_row):
    """Convert a transaction row to tuple.

    Details of fields
        0: 'D',     # Transaction date
        2: 'M',     # Transaction details
        3: 'T',     # Deposit
        4: 'T-',    # Withdrawal
    """
    logger.debug('get_icicicsv: Data row = {}'.format(data_row))
    date = data_row[0].replace('-', '/')
    if _valid_date(date):
        amt = '-{}'.format(data_row[4])
        if data_row[3] != '0':
            amt = data_row[3]
        return Transaction(id=0, date=date, payee='', memo=data_row[2], amount=amt)
    return InvalidTransaction()