def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    login_manager.init_app(app)
    redis.init_app(app)
    db.init_app(app)
    gateway.init_app(app=app)
    celery.conf.update(app.config)

    class ContextTask(celery.Task):

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    from app.ussd import ussd as ussd_bp
    app.register_blueprint(ussd_bp)
    from app.util import setup_logging
    from config import basedir
    if app.debug:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.INFO
    path = os.path.join(basedir, 'app_logger.yaml')
    setup_logging(default_level=logging_level, logger_file_path=path)
    return app