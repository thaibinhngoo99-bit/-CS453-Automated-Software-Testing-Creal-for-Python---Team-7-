def augment_with_sox(original_file, audio_files, augmented_file):
    interfere_file = np.random.choice(audio_files)
    min_SNR = 20
    min_SIR = 5
    signal_gain = round(np.random.uniform(low=-10, high=0), 2)
    signal_params = {'tempo': round(np.random.triangular(left=0.7, mode=1.0, right=1.3), 2), 'pitch': int(round(np.random.triangular(left=-200, mode=0, right=200))), 'reverb': (int(round(np.random.uniform(low=0, high=50))), 50, 100, 100, 0, 0), 'gain -n': signal_gain}
    signal_params.update(build_random_bandpass(1000, 1000, 100))
    interfere_params = {'tempo': round(np.random.uniform(low=0.6, high=1.4), 2), 'pitch': int(round(np.random.uniform(low=-500, high=500))), 'reverb': (int(round(np.random.uniform(low=0, high=100))), 50, 100, 100, 0, 0), 'gain -n': round(np.random.uniform(low=-50, high=signal_gain - min_SIR), 2)}
    interfere_params.update(build_random_bandpass(50, 100, 1000))
    signal = build_sox_distortions(original_file, signal_params)
    interfere_signal = build_sox_distortions(interfere_file, interfere_params)
    noise_power = round(np.random.uniform(-60, signal_gain - min_SNR), 2)
    lowpass = int(round(np.random.uniform(low=100, high=MAX_FREQ)))
    highpass = int(round(np.random.uniform(low=1, high=lowpass)))
    noise = build_sox_noise(original_file, np.random.uniform(0.1, 2), lowpass, highpass, noise_power)
    interf = build_sox_interference(interfere_file, interfere_signal, lowpass_cutoff=np.random.uniform(0.5, 2), ac_gain=int(round(np.random.uniform(-9, -3))))
    sox_cmd = add_signals_trim_to_len(original_file, [signal, noise, interf], augmented_file)
    FNULL = open(os.devnull, 'w')
    subprocess.call(['bash', '-c', sox_cmd], stdout=FNULL, stderr=subprocess.STDOUT)