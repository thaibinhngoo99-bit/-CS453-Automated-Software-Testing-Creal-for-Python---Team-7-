def getClassID(name):
    loadModels = _model(False).query(query={'name': name})['results']
    if loadModels:
        loadModels = loadModels[0]
        return loadModels['_id']
    return None