def select_option_date(avalaiable_dates: List[str], other_args: List[str]) -> str:
    """Select an option date out of a supplied list

    Parameters
    ----------
    avalaiable_dates: List[str]
        Possible date options
    other_args: List[str]
        Arparse arguments
    Returns
    -------
    expiry_date: str
        Selected expiry date
    """
    parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter, prog='exp', description='See and set expiration date')
    parser.add_argument('-d', '--date', dest='n_date', action='store', type=int, default=-1, choices=range(len(avalaiable_dates)), help='Select index for expiry date.')
    parser.add_argument('-D', dest='date', type=str, choices=avalaiable_dates + [''], help='Select date (YYYY-MM-DD)', default='')
    try:
        if other_args:
            if '-' not in other_args[0]:
                other_args.insert(0, '-d')
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return ''
        if ns_parser.n_date == -1 and (not ns_parser.date):
            print('\nAvailable expiry dates:')
            for i, d in enumerate(avalaiable_dates):
                print(f'   {(2 - len(str(i))) * ' '}{i}.  {d}')
            print('')
            return ''
        elif ns_parser.date:
            if ns_parser.date in avalaiable_dates:
                print(f'Expiraration set to {ns_parser.date} \n')
                return ns_parser.date
            else:
                print('Expiration not an option')
                return ''
        else:
            expiry_date = avalaiable_dates[ns_parser.n_date]
            print(f'Expiraration set to {expiry_date} \n')
            return expiry_date
    except Exception as e:
        print(e, '\n')
        return ''