def harvest_oai(**kwargs):
    """Create OAI ListRecords Iterator for Harvesting Data."""
    oai_endpoint = kwargs.get('oai_endpoint')
    harvest_params = kwargs.get('harvest_params')
    logging.info('Harvesting from %s', oai_endpoint)
    logging.info('Harvesting %s', harvest_params)
    sickle = Sickle(oai_endpoint, retry_status_codes=[500, 503], max_retries=3)
    class_mapping = harvest_params.get('class_mapping', {'ListRecords': HarvestRecord})
    iterator = harvest_params.get('iterator', HarvestIterator)
    for key in class_mapping:
        sickle.class_mapping[key] = class_mapping[key]
    sickle.iterator = iterator
    try:
        return sickle.ListRecords(**harvest_params)
    except NoRecordsMatch:
        logging.info('No records found.')
        return []