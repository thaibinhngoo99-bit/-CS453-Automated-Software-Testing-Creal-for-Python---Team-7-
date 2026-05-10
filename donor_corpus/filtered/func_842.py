def handler(signum, frame):
    publish('Offline')
    log.debug('Ende Application')
    exit(0)