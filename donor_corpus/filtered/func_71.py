def build_sox_noise(audio_file, amod_lowpass_cutoff=0.1, lowpass_cutoff=MAX_FREQ, highpass_cutoff=1, noise_gain=-4):
    """
    play original.wav synth whitenoise lowpass 0.1 synth whitenoise amod gain -n 0 lowpass 100 highpass 1
    """
    sox_params = 'sox {audio_file} -p synth whitenoise lowpass {amod_lowpass_cutoff} synth whitenoise amod gain -n {noise_gain} lowpass {lowpass_cutoff} highpass {highpass_cutoff}'.format(audio_file=audio_file, amod_lowpass_cutoff=amod_lowpass_cutoff, lowpass_cutoff=lowpass_cutoff, highpass_cutoff=highpass_cutoff, noise_gain=noise_gain)
    return sox_params