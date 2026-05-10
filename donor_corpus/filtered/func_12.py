def main():
    """Main driver."""
    args = parse_args()
    args.reporter = Reporter()
    check_config(args.reporter, args.source_dir)
    check_source_rmd(args.reporter, args.source_dir, args.parser)
    args.references = read_references(args.reporter, args.reference_path)
    docs = read_all_markdown(args.source_dir, args.parser)
    check_fileset(args.source_dir, args.reporter, list(docs.keys()))
    check_unwanted_files(args.source_dir, args.reporter)
    for filename in list(docs.keys()):
        checker = create_checker(args, filename, docs[filename])
        checker.check()
    args.reporter.report()
    if args.reporter.messages and (not args.permissive):
        exit(1)