def read_groups_from_bam(bam_filename, use_libraries=False):
    bam = pysam.AlignmentFile(bam_filename, 'rb')
    header = bam.header
    results = {}
    if 'RG' in header:
        read_groups = header['RG']
        if use_libraries:
            field = 'LB'
        else:
            field = 'ID'
        for read_group in read_groups:
            results[read_group[field]] = 1
    results_without_duplicates = [key for key, ignored in results.items()]
    sorted_read_groups = sorted(results_without_duplicates)
    return sorted_read_groups