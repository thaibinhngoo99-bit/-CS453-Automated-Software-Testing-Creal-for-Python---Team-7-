def perform_xml_lookup_with_cache():
    cache = {}

    def perform_xml_lookup(oai_record, **kwargs):
        """Parse additions/updates & add boundwiths."""
        if len(cache) == 0:
            logging.info('*** Fetching CSV lookup file from s3 ***')
            access_id = kwargs.get('access_id')
            access_secret = kwargs.get('access_secret')
            bucket = kwargs.get('bucket_name')
            lookup_key = kwargs.get('lookup_key')
            csv_data = process.get_s3_content(bucket, lookup_key, access_id, access_secret)
            cache['value'] = pandas.read_csv(io.BytesIO(csv_data), header=0)
        lookup_csv = cache['value']
        for record in oai_record.xpath('.//marc21:record', namespaces=NS):
            record_id = process.get_record_001(record)
            logging.info('Reading in Record %s', record_id)
            parent_txt = lookup_csv.loc[lookup_csv.child_id == int(record_id), 'parent_xml'].values
            if len(set(parent_txt)) >= 1:
                logging.info('Child XML record found %s', record_id)
                for parent_node in parent_txt[0].split('||'):
                    try:
                        record.append(etree.fromstring(parent_node))
                    except etree.XMLSyntaxError as error:
                        logging.error('Problem with string syntax:')
                        logging.error(error)
                        logging.error(parent_node)
        return oai_record
    return perform_xml_lookup