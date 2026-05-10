def read_xml(xml_path) -> Tuple[Any, Any, Any, Any, Any]:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    assert root.tag == 'Document'
    doc_filename = root.attrib['doc_name']
    doc_id = root.attrib['doc_id']
    m = re.match('(?P<topic_id>\\d+)_(?P<document_number>\\d+)(?P<subtopic>\\w+)\\.xml', doc_filename)
    topic_id = m.group('topic_id')
    subtopic = m.group('subtopic')
    document_number = int(m.group('document_number'))
    documents_index = pd.MultiIndex.from_tuples([(topic_id, subtopic, doc_id)], names=[TOPIC_ID, SUBTOPIC, DOCUMENT_ID])
    documents = pd.DataFrame({DOCUMENT_ID: pd.Series(doc_id, index=documents_index), DOCUMENT_NUMBER: pd.Series(document_number, index=documents_index)})
    contents_rows = []
    contents_index = []
    for token_elmt in root.iter('token'):
        sentence_idx = int(token_elmt.attrib['sentence'])
        token_idx = int(token_elmt.attrib['number'])
        contents_index.append((doc_id, sentence_idx, token_idx))
        token = token_elmt.text
        contents_rows.append({TOKEN: token})
    contents_index = pd.MultiIndex.from_tuples(contents_index, names=[DOCUMENT_ID, SENTENCE_IDX, TOKEN_IDX])
    contents = pd.DataFrame(contents_rows, index=contents_index)
    mentions_rows = []
    mentions_index = []
    entities_events = []
    for markable in root.find('Markables').getchildren():
        if markable.tag == 'UNKNOWN_INSTANCE_TAG':
            continue
        mention_id = int(markable.attrib['m_id'])
        if 'TAG_DESCRIPTOR' in markable.attrib.keys():
            if 'instance_id' in markable.attrib.keys():
                entities_events.append({EVENT: markable.attrib['instance_id'], DESCRIPTION: markable.attrib['TAG_DESCRIPTOR']})
            continue
        token_ids = [int(anchor.attrib['t_id']) for anchor in markable.iter('token_anchor')]
        token_ids_from, token_ids_to = (min(token_ids), max(token_ids))
        token_indexes = contents.index.get_level_values(TOKEN_IDX).values
        token_idx_from = token_indexes[token_ids_from - 1]
        token_idx_to = token_indexes[token_ids_to - 1] + 1
        sentence_idx = contents.index.get_level_values(SENTENCE_IDX).values[token_ids_from - 1]
        is_non_contiguous_mention = len(token_ids) < token_idx_from - token_idx_to
        if is_non_contiguous_mention:
            logger.info('Converted non-contiguous mention to contiguous mention.')
        mentions_index.append((doc_id, mention_id))
        mentions_rows.append({SENTENCE_IDX: sentence_idx, TOKEN_IDX_FROM: token_idx_from, TOKEN_IDX_TO: token_idx_to, MENTION_TYPE: markable.tag})
    mentions_index = pd.MultiIndex.from_tuples(mentions_index, names=[DOCUMENT_ID, MENTION_ID])
    mentions = pd.DataFrame(mentions_rows, index=mentions_index)
    entities_events = pd.DataFrame(entities_events).set_index(EVENT)
    clusters_rows = []
    for relation in root.find('Relations').getchildren():
        tags_of_interest = ['CROSS_DOC_COREF', 'INTRA_DOC_COREF']
        if not relation.tag in tags_of_interest:
            logger.info('Unexpected tag ' + relation.tag)
            raise NotImplementedError
        if 'note' in relation.attrib:
            relation_id = relation.attrib['note']
        else:
            relation_id = doc_id + '_' + relation.attrib['r_id']
        for mention in relation.iter('source'):
            mention_id = int(mention.attrib['m_id'])
            clusters_rows.append({EVENT: relation_id, DOCUMENT_ID: doc_id, MENTION_ID: mention_id})
    clusters = pd.DataFrame(clusters_rows)
    if clusters.empty:
        singletons = mentions.index.to_frame().reset_index(drop=True)
    else:
        outer = pd.merge(mentions, clusters, left_index=True, right_on=[DOCUMENT_ID, MENTION_ID], how='outer')
        singletons = outer.loc[outer[EVENT].isna(), [DOCUMENT_ID, MENTION_ID]]
    singletons[EVENT] = 'SINGLETON_' + singletons.astype(str).apply('_'.join, axis=1)
    clusters = clusters.append(singletons, sort=False).reset_index(drop=True)
    return (documents, contents, mentions, clusters, entities_events)