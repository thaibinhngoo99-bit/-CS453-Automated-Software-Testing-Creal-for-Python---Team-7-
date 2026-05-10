def oai_to_s3(**kwargs):
    """Wrapper function for using OAI Harvest, Default Processor, and S3 Writer."""
    kwargs['harvest_params'] = {'metadataPrefix': kwargs.get('metadata_prefix'), 'from': kwargs.get('harvest_from_date'), 'until': kwargs.get('harvest_until_date')}
    dag_id = kwargs['dag'].dag_id
    dag_start_date = kwargs['timestamp']
    oai_sets = generate_oai_sets(**kwargs)
    all_processed = []
    sets_with_no_records = []
    if oai_sets:
        for oai_set in oai_sets:
            kwargs['harvest_params']['set'] = oai_set
            data = harvest_oai(**kwargs)
            if data == []:
                sets_with_no_records.append(oai_set)
                logging.info('Skipping processing % set because it has no data.', oai_set)
                continue
            outdir = dag_s3_prefix(dag_id, dag_start_date)
            processed = process_xml(data, dag_write_string_to_s3, outdir, **kwargs)
            all_processed.append(processed)
    else:
        data = harvest_oai(**kwargs)
        if data == []:
            sets_with_no_records.append(oai_set)
        outdir = dag_s3_prefix(dag_id, dag_start_date)
        processed = process_xml(data, dag_write_string_to_s3, outdir, **kwargs)
        all_processed.append(processed)
    all_updated = sum([set['updated'] for set in all_processed])
    all_deleted = sum([set['deleted'] for set in all_processed])
    logging.info('Total OAI Records Harvested & Processed: %s', all_updated)
    logging.info('Total OAI Records Harvest & Marked for Deletion: %s', all_deleted)
    logging.info('Total sets with no records: %s', len(sets_with_no_records))
    logging.info('Sets with no records %s', sets_with_no_records)
    return {'updated': all_updated, 'deleted': all_deleted, 'sets_with_no_records': sets_with_no_records}