def proc_fmap(config, args, func_refs=None):
    refs = dict()
    for scan in iterconfig(config, 'fmap'):
        ref = scan.get('id', None)
        templ = 'sub-${sub}_ses-${ses}'
        if 'acquisition' in scan:
            templ += '_acq-${acquisition}'
        if 'run' in scan:
            templ += '_run-${run}'
        if 'direction' in scan:
            templ += '_dir-${direction}'
        templ += '_${modality}'
        templ = string.Template(templ)
        fbase = templ.safe_substitute(sub=legal.sub('', args.subject), ses=legal.sub('', args.session), acquisition=scan.get('acquisition', None), run=scan.get('run', None), direction=scan.get('direction', None), modality=scan.get('modality', None))
        sourcedata_dir = os.path.join(args.sourcedata, scan['type'])
        if not os.path.exists(sourcedata_dir):
            os.makedirs(sourcedata_dir)
        dicom_dir = os.path.join(sourcedata_dir, '{0}.dicom'.format(fbase))
        logger.info('downloading session=%s, scan=%s, loc=%s', args.session, scan['scan'], dicom_dir)
        args.xnat.download(args.session, [scan['scan']], out_dir=dicom_dir)
        fname = '{0}.nii.gz'.format(fbase)
        refs[ref] = os.path.join(scan['type'], fname)
        fullfile = os.path.join(args.bids, scan['type'], fname)
        logger.info('converting %s to %s', dicom_dir, fullfile)
        convert(dicom_dir, fullfile)
        if scan['type'] == 'fmap':
            if scan.get('modality', None) == 'magnitude':
                rename_fmapm(args.bids, fbase)
            elif scan.get('modality', None) == 'phase':
                rename_fmapp(args.bids, fbase)
        sidecar_file = os.path.join(args.bids, scan['type'], fbase + '.json')
        with open(sidecar_file, 'r') as fo:
            sidecarjs = json.load(fo)
        sidecarjs['DataSource'] = {'application/x-xnat': {'url': args.xnat.url, 'project': args.project, 'subject': args.subject, 'subject_id': args.subject_id, 'experiment': args.session, 'experiment_id': args.session_id, 'scan': scan['scan']}}
        if 'intended for' in scan and func_refs:
            for intended in scan['intended for']:
                if intended in func_refs:
                    logger.info('adding IntendedFor %s to %s', func_refs[intended], sidecar_file)
                    if 'IntendedFor' not in sidecarjs:
                        sidecarjs['IntendedFor'] = list()
                    if func_refs[intended] not in sidecarjs['IntendedFor']:
                        sidecarjs['IntendedFor'].append(func_refs[intended])
            logger.info('writing file %s', sidecar_file)
        commons.atomic_write(sidecar_file, json.dumps(sidecarjs, indent=2))
    return refs