def read_split_data(root: Path, sentence_filter_csv: Optional[Path]):
    documents = []
    contents = []
    mentions = []
    clusters = []
    entities_events = []
    for root, dirs, files in os.walk(str(root.absolute())):
        for file in files:
            path = os.path.abspath(os.path.join(root, file))
            f_documents, f_contents, f_mentions, f_clusters, f_entities_events = read_xml(path)
            documents.append(f_documents)
            contents.append(f_contents)
            mentions.append(f_mentions)
            clusters.append(f_clusters)
            entities_events.append(f_entities_events)
    documents = pd.concat(documents).sort_index()
    contents = pd.concat(contents).sort_index()
    mentions = pd.concat(mentions).sort_index()
    clusters = pd.concat(clusters, sort=False)
    entities_events = pd.concat(entities_events).sort_index()
    assert clusters.duplicated(subset=[DOCUMENT_ID, MENTION_ID]).value_counts().get(True, 0) == 0
    clusters = clusters.set_index([DOCUMENT_ID, MENTION_ID])
    mentions = pd.merge(mentions, clusters, left_index=True, right_index=True).sort_index()
    if sentence_filter_csv is not None:
        sent_filter = pd.read_csv(sentence_filter_csv)
        doc_number_and_subtopic = sent_filter['File'].str.split('ecb', expand=True)
        doc_number_and_subtopic.columns = [DOCUMENT_NUMBER, SUBTOPIC]
        doc_number_and_subtopic[DOCUMENT_NUMBER] = doc_number_and_subtopic[DOCUMENT_NUMBER].astype(int)
        doc_number_and_subtopic[SUBTOPIC].replace({'plus': 'ecbplus', '': 'ecb'}, inplace=True)
        sent_filter = pd.concat([sent_filter.drop(columns='File'), doc_number_and_subtopic], axis=1)
        sent_filter.rename(columns={'Topic': TOPIC_ID, 'Sentence Number': SENTENCE_IDX}, inplace=True)
        sent_filter[TOPIC_ID] = sent_filter[TOPIC_ID].astype(str)
        sent_filter = sent_filter[[TOPIC_ID, SUBTOPIC, DOCUMENT_NUMBER, SENTENCE_IDX]]
        topics_in_split = documents.index.get_level_values(TOPIC_ID).unique()
        sent_filter = sent_filter.loc[sent_filter[TOPIC_ID].isin(topics_in_split)].copy()
        documents_with_doc_number_in_index = documents.set_index(DOCUMENT_NUMBER, append=True).reset_index(level=DOCUMENT_ID, drop=True).sort_index()
        sent_filter[DOCUMENT_ID] = sent_filter[[TOPIC_ID, SUBTOPIC, DOCUMENT_NUMBER]].apply(lambda row: documents_with_doc_number_in_index[DOCUMENT_ID].loc[tuple(row.values)], axis=1)
        all_mentions_to_keep = []
        for doc_id, df in mentions.groupby(DOCUMENT_ID):
            sentences_to_keep = sent_filter.loc[sent_filter[DOCUMENT_ID] == doc_id]
            is_official_evaluation_sentence = df[SENTENCE_IDX].isin(sentences_to_keep[SENTENCE_IDX])
            is_action_mention = df[MENTION_TYPE].isin(MENTION_TYPES_ACTION)
            mentions_to_keep = df.loc[is_official_evaluation_sentence | ~is_action_mention]
            all_mentions_to_keep.append(mentions_to_keep)
        mentions = pd.concat(all_mentions_to_keep).sort_index()
    return (documents, contents, mentions, entities_events)