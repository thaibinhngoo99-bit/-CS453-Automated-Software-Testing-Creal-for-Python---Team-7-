def check_fileset(source_dir, reporter, filenames_present):
    """Are all required files present? Are extraneous files present?"""
    required = [p.replace('%', source_dir) for p in REQUIRED_FILES]
    missing = set(required) - set(filenames_present)
    for m in missing:
        reporter.add(None, 'Missing required file {0}', m)
    seen = []
    for filename in filenames_present:
        if '_episodes' not in filename:
            continue
        m = P_EPISODE_FILENAME.search(filename)
        if m and m.group(1):
            seen.append(m.group(1))
        else:
            reporter.add(None, 'Episode {0} has badly-formatted filename', filename)
    reporter.check(len(seen) == len(set(seen)), None, 'Duplicate episode numbers {0} vs {1}', sorted(seen), sorted(set(seen)))
    seen = sorted([int(s) for s in seen])
    clean = True
    for i in range(len(seen) - 1):
        clean = clean and seen[i + 1] - seen[i] == 1
    reporter.check(clean, None, 'Missing or non-consecutive episode numbers {0}', seen)