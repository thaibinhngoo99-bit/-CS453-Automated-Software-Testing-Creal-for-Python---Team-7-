def deregisterModel(name, className, classType, location):
    loadModels = _model(False).query(query={'name': name})['results']
    if loadModels:
        loadModels = loadModels[0]
        results = _model().api_delete(query={'name': name, 'classType': classType})
        if results['result']:
            return True
    if jimi.logging.debugEnabled:
        jimi.logging.debug("deregister model failed modelName='{0}', className='{1}', classType='{2}', location='{3}'".format(name, className, classType, location), 4)