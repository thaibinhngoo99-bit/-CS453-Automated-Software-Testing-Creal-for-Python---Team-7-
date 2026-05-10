def proc_anat(config, args):
    """
    Download anatomical data and convert to BIDS
    """
    refs = dict()
    for scan in iterconfig(config, 'anat'):
        ref = scan.get('id', None)
        templ = 'sub-${sub}_ses-${ses}'
        if 'acquisition' in scan:
            templ += '_acq-${acquisition}'
        if 'run' in scan:
            templ += '_run-${run}'
        templ += '_${modality}'
        templ = string.Template(templ)
        fbase = templ.safe_substitute(sub=legal.sub('', args.subject), ses=legal.sub('', args.session), acquisition=scan.get('acquisition', None), run=scan.get('run', None), modality=scan.get('modality', None))
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
        modality = scan.get('modality', None)
        sidecar_files = list()
        if modality == 'T1vnav':
            fullfile = fullfile.replace('_T1vnav', '_split-%r_T1vnav')
            for f in glob.glob(os.path.join(dicom_dir, '*.dcm')):
                logger.debug('converting single file %s to %s', f, fullfile)
                convert(f, fullfile, single_file=True)
            ffbase = re.sub('.nii(.gz)?', '', fullfile)
            expr = ffbase.replace('%r', '*') + '.json'
            logger.debug('globbing for %s', expr)
            sidecar_files = glob.glob(expr)
        else:
            convert(dicom_dir, fullfile)
            sidecar_files = [os.path.join(args.bids, scan['type'], fbase + '.json')]
        for sidecar_file in sidecar_files:
            logger.debug('adding provenance to %s', sidecar_file)
            with open(sidecar_file) as fo:
                sidecarjs = json.load(fo)
            sidecarjs['DataSource'] = {'application/x-xnat': {'url': args.xnat.url, 'project': args.project, 'subject': args.subject, 'subject_id': args.subject_id, 'experiment': args.session, 'experiment_id': args.session_id, 'scan': scan['scan']}}
            commons.atomic_write(sidecar_file, json.dumps(sidecarjs, indent=2))
    return refs