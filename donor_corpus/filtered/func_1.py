def save_amplitudes(self, key, params, pershot=False, conditional=False):
    """Save complex statevector amplitudes.

    Args:
        key (str): the key for retrieving saved data from results.
        params (List[int] or List[str]): the basis states to return amplitudes for.
        pershot (bool): if True save a list of amplitudes vectors for each
                        shot of the simulation rather than the a single
                        amplitude vector [Default: False].
        conditional (bool): if True save the amplitudes vector conditional
                            on the current classical register values
                            [Default: False].

    Returns:
        QuantumCircuit: with attached instruction.

    Raises:
        ExtensionError: if params is invalid for the specified number of qubits.
    """
    qubits = default_qubits(self)
    instr = SaveAmplitudes(key, len(qubits), params, pershot=pershot, conditional=conditional)
    return self.append(instr, qubits)