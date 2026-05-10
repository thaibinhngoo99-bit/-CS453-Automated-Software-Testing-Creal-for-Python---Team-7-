def readingTestCorpus(test_file_path):
    print('reading...')
    test_file = open(test_file_path, 'r')
    list_pairs = []
    tmp_pair = []
    for line in test_file:
        line = line.strip('\n')
        if line == sub:
            list_pairs.append(tmp_pair)
            tmp_pair = []
        else:
            tmp_pair.append(line)
    test_file.close()
    test_contexts = []
    test_replys = []
    max_con_size = 0
    min_con_size = 10000
    for pair in list_pairs:
        if len(pair) >= 3:
            test_contexts.append(pair[0:-1])
            test_replys.append(pair[-1])
            max_con_size = max(len(pair[0:-1]), max_con_size)
            min_con_size = min(len(pair[0:-1]), min_con_size)
        else:
            pass
    print(max_con_size)
    print(min_con_size)
    return (test_contexts, test_replys)