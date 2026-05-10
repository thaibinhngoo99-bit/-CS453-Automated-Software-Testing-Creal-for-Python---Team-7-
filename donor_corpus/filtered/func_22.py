def loadModel(modelName):
    results = _model(False).query(query={'name': modelName})['results']
    if len(results) == 1:
        results = results[0]
        _class = _model().get(results['_id'])
        return _class
    return None