def bids_from_config(yaxil_session, scans_metadata, config, out_base):
    """
    Create a BIDS output directory from configuration file
    """
    _item = next(iter(scans_metadata))
    project, session, subject = (_item['session_project'], _item['session_label'], _item['subject_label'])
    session_id, subject_id = (_item['session_id'], _item['subject_id'])
    check_dataset_description(out_base)
    sourcedata_base = os.path.join(out_base, 'sourcedata', 'sub-{0}'.format(legal.sub('', subject)), 'ses-{0}'.format(legal.sub('', session)))
    bids_base = os.path.join(out_base, 'sub-{0}'.format(legal.sub('', subject)), 'ses-{0}'.format(legal.sub('', session)))
    args = commons.struct(xnat=yaxil_session, subject=subject, subject_id=subject_id, session=session, session_id=session_id, project=project, bids=bids_base, sourcedata=sourcedata_base)
    func_refs = proc_func(config, args)
    anat_refs = proc_anat(config, args)
    dwi_refs = proc_dwi(config, args)
    fmap_refs = proc_fmap(config, args, func_refs)