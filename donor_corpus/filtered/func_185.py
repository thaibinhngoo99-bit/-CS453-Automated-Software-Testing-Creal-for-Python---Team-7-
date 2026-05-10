def get_labels(load_label_table):
    with open(load_label_table) as f:
        label_table = f.readlines()
        label_table = np.asarray(label_table)
    ggo = []
    cons = []
    pe = []
    for line in label_table:
        label = line.split()[0]
        if label.isnumeric():
            if 'Background' in line or 'background' in line:
                continue
            infection = line.split('_')[1]
            keywords = ['ggo', 'gg']
            if any((x in infection.lower() for x in keywords)):
                ggo.append(int(label))
            keywords = ['cons', 'cns', 'con', 'cos', 'co']
            if any((x in infection.lower() for x in keywords)):
                cons.append(int(label))
            keywords = ['pe', 'pes']
            if any((x in infection.lower() for x in keywords)):
                pe.append(int(label))
    return (ggo, cons, pe)