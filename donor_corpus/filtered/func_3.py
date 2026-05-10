def _format_amplitude_params(params, num_qubits=None):
    """Format amplitude params as a interger list."""
    if isinstance(params[0], str):
        if params[0].find('0x') == 0:
            params = [int(i, 16) for i in params]
        else:
            params = [int(i, 2) for i in params]
    if num_qubits and max(params) >= 2 ** num_qubits:
        raise ExtensionError('Param values contain a state larger than the number of qubits')
    return params