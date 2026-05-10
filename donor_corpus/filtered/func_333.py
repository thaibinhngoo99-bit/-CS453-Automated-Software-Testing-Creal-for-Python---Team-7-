def to_manifest(items: Iterable[ManifestItem]) -> Optional[Manifest]:
    """
    Take an iterable of data types in Lhotse such as Recording, SupervisonSegment or Cut, and create the manifest of the
    corresponding type. When the iterable is empty, returns None.
    """
    items = iter(items)
    try:
        first_item = next(items)
    except StopIteration:
        return None
    items = chain([first_item], items)
    if isinstance(first_item, Recording):
        return RecordingSet.from_recordings(items)
    if isinstance(first_item, SupervisionSegment):
        return SupervisionSet.from_segments(items)
    if isinstance(first_item, (Cut, MixedCut)):
        return CutSet.from_cuts(items)
    if isinstance(first_item, Features):
        raise ValueError('FeatureSet generic construction from iterable is not possible, as the config information would have been lost. Call FeatureSet.from_features() directly instead.')
    raise ValueError(f'Unknown type of manifest item: {first_item}')