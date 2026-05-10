def read_outcomes(path):
    cases = []
    headers = []
    with open(path, 'rb') as csvfile:
        reader = csvfile.readlines()
        n = len(reader[0].split())
        for i, row in enumerate(reader):
            cases.append(int(row))
    return cases