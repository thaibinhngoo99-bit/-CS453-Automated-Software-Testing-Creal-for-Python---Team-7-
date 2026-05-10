def process_xml(data, writer, outdir, **kwargs):
    """Process & Write XML data to S3."""
    parser = kwargs.get('parser')
    records_per_file = kwargs.get('records_per_file')
    if kwargs.get('dag'):
        run_id = kwargs.get('dag').dag_id
    else:
        run_id = 'no-dag-provided'
    if kwargs.get('timestamp'):
        timestamp = kwargs.get('timestamp')
    else:
        timestamp = 'no-timestamp-provided'
    if not records_per_file:
        records_per_file = 1000
    count = deleted_count = 0
    oai_updates = OaiXml(run_id, timestamp)
    oai_deletes = OaiXml(run_id, timestamp)
    logging.info('Processing XML')
    for record in data:
        record_id = record.header.identifier
        record = record.xml
        record.attrib['airflow-record-id'] = record_id
        if parser:
            record = parser(record, **kwargs)
        if record.xpath(".//oai:header[@status='deleted']", namespaces=NS):
            logging.info('Added record %s to deleted xml file(s)', record_id)
            deleted_count += 1
            oai_deletes.append(record)
            if deleted_count % int(records_per_file) == 0:
                writer(oai_deletes.tostring(), outdir + '/deleted', **kwargs)
                oai_deletes = OaiXml(run_id, timestamp)
        else:
            logging.info('Added record %s to new-updated xml file', record_id)
            count += 1
            oai_updates.append(record)
            if count % int(records_per_file) == 0:
                writer(oai_updates.tostring(), outdir + '/new-updated', **kwargs)
                oai_updates = OaiXml(run_id, timestamp)
    writer(oai_updates.tostring(), outdir + '/new-updated', **kwargs)
    writer(oai_deletes.tostring(), outdir + '/deleted', **kwargs)
    logging.info('OAI Records Harvested & Processed: %s', count)
    logging.info('OAI Records Harvest & Marked for Deletion: %s', deleted_count)
    return {'updated': count, 'deleted': deleted_count}