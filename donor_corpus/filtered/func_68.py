def process_chime(source=hp.whole_chime_path, target=hp.part_chime_path, sr=16000, duration=30, count=10):
    """
    Randomly picking segments from CHiME dataset, since full dataset is not necessary in our case.
    :param source:
    :param target:
    :param sr:
    :param duration:
    :param count:
    :return:
    """
    makedirs(str(target), exist_ok=True)
    for path in tqdm(source.glob('*.wav')):
        wave = load_wav(path, sr)
        if len(wave) < sr * 30:
            continue
        waves = get_segments(wave, duration * sr, count)
        for i, wave in enumerate(waves, 1):
            save_wav(wave, str(target / f'{path.stem}_{i}.wav'), sr)