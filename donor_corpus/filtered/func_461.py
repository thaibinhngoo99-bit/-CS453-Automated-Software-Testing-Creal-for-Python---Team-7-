def _get_nrf_device_args(options):
    nrfjprog_args = ['nrfjprog', '--ids']
    nrfjprog_ids = subprocess.check_output(nrfjprog_args, encoding='utf-8')
    if not nrfjprog_ids.strip('\n'):
        raise BoardAutodetectFailed(f'No attached boards recognized by {' '.join(nrfjprog_args)}')
    boards = nrfjprog_ids.split('\n')[:-1]
    if len(boards) > 1:
        if options['nrfjprog_snr'] is None:
            raise BoardError(f'Multiple boards connected; specify one with nrfjprog_snr=: {', '.join(boards)}')
        if str(options['nrfjprog_snr']) not in boards:
            raise BoardError(f'nrfjprog_snr ({options['nrfjprog_snr']}) not found in {nrfjprog_args}: {boards}')
        return ['--snr', options['nrfjprog_snr']]
    if not boards:
        return []
    return ['--snr', boards[0]]