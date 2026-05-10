def voi(other_args: List[str]):
    """Parse Volume + open interest argparse

    Parameters
    ----------
    other_args: List[str]
        Argparse arguments

    Returns
    -------
    ns_parser: argparse.Namespace
        Parsed namespace
    """
    parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter, prog='voi', description='\n                Plots Volume + Open Interest of calls vs puts.\n            ')
    parser.add_argument('-v', '--minv', dest='min_vol', type=check_non_negative, default=-1, help='minimum volume (considering open interest) threshold of the plot.')
    parser.add_argument('-m', '--min', dest='min_sp', type=check_non_negative, default=-1, help='minimum strike price to consider in the plot.')
    parser.add_argument('-M', '--max', dest='max_sp', type=check_non_negative, default=-1, help='maximum strike price to consider in the plot.')
    parser.add_argument('--source', type=str, default='tr', choices=['tr', 'yf'], dest='source', help='Source to get data from')
    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return None
        return ns_parser
    except Exception as e:
        print(e, '\n')
        return None