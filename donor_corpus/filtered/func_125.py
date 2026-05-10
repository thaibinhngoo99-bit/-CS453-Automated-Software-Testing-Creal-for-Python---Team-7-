def get_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description='Mixing wav.scp files into a multi-channel wav.scp using sox.')
    parser.add_argument('scp', type=str, nargs='+', help='Give wav.scp')
    parser.add_argument('out', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='The output filename. If omitted, then output to sys.stdout')
    return parser