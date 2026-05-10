def generate_oai_sets(**kwargs):
    """Generate the oai sets we want to harvest."""
    all_sets = bool(kwargs.get('all_sets'))
    included_sets = kwargs.get('included_sets')
    excluded_sets = kwargs.get('excluded_sets')
    oai_endpoint = kwargs.get('oai_endpoint')
    if all_sets:
        logging.info('Seeing All Sets Needed.')
        return []
    elif included_sets:
        logging.info('Seeing SetSpec List.')
        if not isinstance(included_sets, list):
            return [included_sets]
        return included_sets
    elif excluded_sets:
        logging.info('Seeing Excluded SetSpec List.')
        if not isinstance(excluded_sets, list):
            excluded_sets = [excluded_sets]
        list_sets = Sickle(oai_endpoint).ListSets()
        all_sets = [oai_set.xml.find('oai:setSpec', namespaces=NS).text for oai_set in list_sets]
        remaining_sets = list(set(all_sets) - set(excluded_sets))
        logging.info(remaining_sets)
        return remaining_sets
    return []