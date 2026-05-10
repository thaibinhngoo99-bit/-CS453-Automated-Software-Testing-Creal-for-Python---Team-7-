def buildGraphParser(opts, dummyBuilder, reprBuilder):
    reprDim = reprBuilder.getDim()
    tokExtractors, featBuilders = buildGraphFeatureExtractors(opts.features, reprDim)
    extractor = gfeatures.GraphFeatureExtractor(tokExtractors)
    featIds = extractor.getFeatIds() + [feat.getFeatId() for feat in featBuilders.values()]
    network = imsnpars.nparser.network.ParserNetwork(opts.mlpHiddenDim, opts.nonLinFun, featIds)
    featBuilder = imsnpars.nparser.features.FeatReprBuilder(extractor, featBuilders, dummyBuilder, network, opts.parseLayer)
    mstAlg, decod = buildMSTDecoder(opts, featBuilder)
    if opts.labeler == 'graph':
        lblDict = ltask.LblTagDict()
        parsingTask = task.NNGraphParsingTaskWithLbl(mstAlg, featBuilder, decod, network, opts.augment, lblDict)
    else:
        parsingTask = task.NNGraphParsingTask(mstAlg, featBuilder, decod, network, opts.augment)
    return parsingTask