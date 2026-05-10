def add_signals_trim_to_len(original, signals, augmented):
    signals_to_add = ' '.join(['<(%s)' % s for s in signals])
    sox_cmd = 'sox -m {signals} -b 16 {augmented} trim 0 $(soxi -D {original})'.format(signals=signals_to_add, original=original, augmented=augmented)
    return sox_cmd