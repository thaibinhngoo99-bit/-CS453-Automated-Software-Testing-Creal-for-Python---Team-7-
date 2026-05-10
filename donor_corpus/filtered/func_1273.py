def buildGraphFeatureExtractors(featuresD, reprDim):
    featIds = {('h', '0'): gfeatures.FeatId.HEAD, ('d', '0'): gfeatures.FeatId.DEP, ('h', '1'): gfeatures.FeatId.HEAD_P_1, ('h', '2'): gfeatures.FeatId.HEAD_P_2, ('d', '1'): gfeatures.FeatId.DEP_P_1, ('d', '2'): gfeatures.FeatId.DEP_P_2, ('h', '-1'): gfeatures.FeatId.HEAD_M_1, ('h', '-2'): gfeatures.FeatId.HEAD_M_2, ('d', '-1'): gfeatures.FeatId.DEP_M_1, ('d', '-2'): gfeatures.FeatId.DEP_M_2, ('dist', '0'): gfeatures.FeatId.DIST}
    mainFeatIds = {'h': gfeatures.FeatId.HEAD, 'd': gfeatures.FeatId.DEP}
    featureExtractors = {}
    featureBuilders = {}
    for feat in featuresD:
        if '+' in feat:
            name, shift = feat.split('+')
        elif '-' in feat:
            name, shift = feat.split('-')
            shift = '-' + shift
        else:
            name, shift = (feat, '0')
        featId = featIds.get((name, shift))
        if featId == None:
            logging.error('Unknown token id: %s' % feat)
            sys.exit()
        if featId == gfeatures.FeatId.DIST:
            featureBuilders[featId] = gfeatures.DistFeatureBuilder(reprDim)
        else:
            mainFeature = mainFeatIds[name]
            if mainFeature not in featureExtractors:
                featureExtractors[mainFeature] = gfeatures.TokenFeatExtractor()
            featureExtractors[mainFeature].addShift(featId, int(shift))
    return (featureExtractors, featureBuilders)