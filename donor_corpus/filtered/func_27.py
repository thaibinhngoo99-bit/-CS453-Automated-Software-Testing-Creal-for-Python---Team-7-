def setup_handlers(lab_app: LabApp):
    setup_globals(lab_app)
    web_app, logger = (lab_app.web_app, lab_app.log)
    apply_api_endpoint_override(logger)
    host_pattern = '.*$'
    handlers = [(url_pattern(web_app, 'check-function'), CheckFunctionSetHandler), (url_pattern(web_app, 'resources'), ResourceHandler), (url_pattern(web_app, 'submit-job'), SubmitJobHandler), (url_pattern(web_app, 'get-env'), EnvironmentHandler)]
    web_app.add_handlers(host_pattern, handlers)
    for h in handlers:
        logger.info('handler => {}'.format(h))