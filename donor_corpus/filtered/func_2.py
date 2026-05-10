def save_amplitudes_squared(self, key, params, unnormalized=False, pershot=False, conditional=False):
    """Save squared statevector amplitudes (probabilities).

    Args:
        key (str): the key for retrieving saved data from results.
        params (List[int] or List[str]): the basis states to return amplitudes for.
        unnormalized (bool): If True return save the unnormalized accumulated
                             probabilities over all shots [Default: False].
        pershot (bool): if True save a list of probability vectors for each
                        shot of the simulation rather than the a single
                        amplitude vector [Default: False].
        conditional (bool): if True save the probability vector conditional
                            on the current classical register values
                            [Default: False].

    Returns:
        QuantumCircuit: with attached instruction.

    Raises:
        ExtensionError: if params is invalid for the specified number of qubits.
    """
    qubits = default_qubits(self)
    instr = SaveAmplitudesSquared(key, len(qubits), params, unnormalized=unnormalized, pershot=pershot, conditional=conditional)
    return self.append(instr, qubits)