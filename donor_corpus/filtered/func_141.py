def setup_logger():
    console = logging.StreamHandler(sys.stdout)
    handlers = [console]
    logging.basicConfig(handlers=handlers)
    root = logging.getLogger()
    root.setLevel(logging.INFO)