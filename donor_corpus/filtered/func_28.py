def setup_globals(lab_app):
    global NOTEBOOK_DIR
    NOTEBOOK_DIR = lab_app.notebook_dir
    lab_app.log.info('setup globals')
    lab_app.log.info('\tNOTEBOOK_DIR: ' + NOTEBOOK_DIR)