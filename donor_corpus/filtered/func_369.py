@click.command()
@click.argument('doc', type=click.Path(exists=True))
@click.option('--profile', prompt='Choose a profile', default='icici', show_default=True, type=click.Choice(['icici', 'icicicc']), help='Document type profile.')
@click.option('--debug', is_flag=True, show_default=True, help='Show diagnostic messages.')
def start(doc, profile, debug):
    """Bout (read bank-out) extracts transactions from csv bank statements."""
    if debug:
        logging.basicConfig(level=logging.DEBUG)
        logger.info('Verbose messages are enabled.')
    profiles.update({'icici': get_icici_csv, 'icicicc': get_icicicc_csv})
    rows = []
    if profile == 'icici':
        header = 'DATE,MODE,PARTICULARS,DEPOSITS,WITHDRAWALS,BALANCE'
        rows = _filter_csv_header(doc, header)
    elif profile == 'icicicc':
        header = 'Date,Sr.No.,Transaction Details,Reward Point Header,Intl.Amount,Amount(in Rs),BillingAmountSign'
        rows = _filter_csv_header(doc, header)
    create_transaction = profiles[profile]
    print_header = False
    for r in rows:
        transaction = create_transaction(r)
        if type(transaction) is not InvalidTransaction:
            if not print_header:
                qif_header()
                print_header = True
            click.echo(to_qif(transaction))