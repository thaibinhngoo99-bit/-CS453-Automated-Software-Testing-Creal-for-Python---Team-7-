def build_varying_amplitude_factor(audio_file, lowpass_cutoff=1, ac_gain=-9):
    ac = 'sox {} -p synth whitenoise lowpass {} gain -n {}'.format(audio_file, lowpass_cutoff, ac_gain)
    dc = 'sox {} -p gain -90 dcshift 0.5'.format(audio_file)
    return 'sox -m <({}) <({}) -p'.format(ac, dc)