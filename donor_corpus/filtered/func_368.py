def _filter_csv_header(doc, header):
    head_skip = False
    mem = io.StringIO()
    with open(doc, encoding='utf-8', mode='r') as f:
        for line in f:
            if line.startswith(header):
                head_skip = True
                continue
            if head_skip and (not line or line.isspace()):
                break
            if head_skip and ',' in line:
                mem.write(line)
    mem.seek(0)
    return csv.reader(mem)