def load_manifest(path: Pathlike) -> Manifest:
    """Generic utility for reading an arbitrary manifest."""
    raw_data = load_yaml(path)
    data_set = None
    for manifest_type in [RecordingSet, SupervisionSet, FeatureSet, CutSet]:
        try:
            data_set = manifest_type.from_dicts(raw_data)
        except Exception:
            pass
    if data_set is None:
        raise ValueError(f'Unknown type of manifest: {path}')
    return data_set