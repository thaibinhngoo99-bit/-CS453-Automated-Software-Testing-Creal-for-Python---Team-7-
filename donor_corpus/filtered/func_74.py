def build_random_bandpass(min_low=50, min_band_width=100, max_high=1000) -> Dict:
    d = {}
    max_high_cutoff = MAX_FREQ
    if np.random.choice([True, False], p=[0.5, 0.5]):
        lowpass = int(round(np.random.uniform(low=min_low, high=MAX_FREQ)))
        d['lowpass'] = lowpass
        max_high_cutoff = lowpass - min_band_width
    if np.random.choice([True, False], p=[0.5, 0.5]):
        highpass = int(round(np.random.uniform(low=1, high=min(max_high, max_high_cutoff))))
        d['highpass'] = highpass
    return d