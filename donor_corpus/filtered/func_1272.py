def buildMSTDecoder(opts, featBuilder):
    if opts.mst == 'CLE':
        mstAlg = cle.ChuLiuEdmonds()
        decod = decoder.FirstOrderDecoder(featBuilder)
    else:
        logging.error('Unknown algorithm: %s' % opts.mst)
        sys.exit()
    logging.info('Graph system used: %s' % type(mstAlg))
    logging.info('Decoder used: %s' % type(decod))
    return (mstAlg, decod)