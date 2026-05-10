def augment_with_specific_params():
    signal_gain = 0
    signal_params = dict(tempo=1.0, pitch=0, reverb=0)
    signal_params['gain -n'] = 0
    signal = build_sox_distortions(original, signal_params)
    interfere_signal = build_sox_distortions(interfering, dict(gain=signal_gain - 10, tempo=0.8, pitch=100, reverb=50))
    noise = build_sox_noise(original, noise_gain=signal_gain - 20, lowpass_cutoff=6000, highpass_cutoff=10)
    interf = build_sox_interference(interfering, interfere_signal)
    sox_cmd = add_signals_trim_to_len(original, [signal, noise, interf], augmented)
    subprocess.call(['bash', '-c', sox_cmd])