def read_groups_and_libraries_from_bam(bam_filename):
    bam = pysam.AlignmentFile(bam_filename, 'rb')
    header = bam.header
    results = {}
    if 'RG' in header:
        read_groups = header['RG']
        for read_group in read_groups:
            read_group_id = read_group['ID']
            read_group_library = read_group['LB']
            results[read_group_id] = read_group_library
    return results