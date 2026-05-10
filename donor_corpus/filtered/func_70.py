def build_sox_distortions(audio_file, params):
    param_str = ' '.join([k + ' ' + to_str(v) for k, v in params.items()])
    sox_params = 'sox {} -p {} '.format(audio_file, param_str)
    return sox_params