def prepare_service(argv=None):
    if argv is None:
        argv = []
    rpc.set_defaults(control_exchange='sysinv')
    cfg.set_defaults(log.log_opts, default_log_levels=['amqplib=WARN', 'qpid.messaging=INFO', 'sqlalchemy=WARN', 'keystoneclient=INFO', 'stevedore=INFO', 'eventlet.wsgi.server=WARN'])
    cfg.CONF(argv[1:], project='sysinv')
    log.setup('sysinv')