def parse_args():
    """Parse command-line arguments."""
    parser = ArgumentParser(description='Check episode files in a lesson.')
    parser.add_argument('-l', '--linelen', default=False, action='store_true', dest='line_lengths', help='Check line lengths')
    parser.add_argument('-p', '--parser', default=None, dest='parser', help='path to Markdown parser')
    parser.add_argument('-r', '--references', default=None, dest='reference_path', help='path to Markdown file of external references')
    parser.add_argument('-s', '--source', default=os.curdir, dest='source_dir', help='source directory')
    parser.add_argument('-w', '--whitespace', default=False, action='store_true', dest='trailing_whitespace', help='Check for trailing whitespace')
    parser.add_argument('--permissive', default=False, action='store_true', dest='permissive', help='Do not raise an error even if issues are detected')
    args, extras = parser.parse_known_args()
    require(args.parser is not None, 'Path to Markdown parser not provided')
    require(not extras, 'Unexpected trailing command-line arguments "{0}"'.format(extras))
    return args