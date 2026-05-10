def vol(other_args: List[str]):
    """Parse volume argparse

    Parameters
    ----------
    other_args: List[str]
        Argparse arguments

    Returns
    -------
    ns_parser: argparse.Namespace
        Parsed namespace
    """
    parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter, prog='vol', description='Plot volume.  Volume refers to the number of contracts traded today.')
    parser.add_argument('-m', '--min', default=-1, type=check_non_negative, help='Min strike to plot', dest='min')
    parser.add_argument('-M', '--max', default=-1, type=check_non_negative, help='Max strike to plot', dest='max')
    parser.add_argument('--calls', action='store_true', default=False, dest='calls', help='Flag to plot call options only')
    parser.add_argument('--puts', action='store_true', default=False, dest='puts', help='Flag to plot put options only')
    parser.add_argument('--source', type=str, default='tr', choices=['tr', 'yf'], dest='source', help='Source to get data from')
    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return
        return ns_parser
    except Exception as e:
        print(e, '\n')