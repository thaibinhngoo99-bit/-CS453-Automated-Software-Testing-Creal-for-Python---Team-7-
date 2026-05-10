def set_incremental_state(module: MultiheadAttention, incremental_state: Optional[Dict[str, Dict[str, Optional[Tensor]]]], key: str, value: Dict[str, Optional[Tensor]]) -> Optional[Dict[str, Dict[str, Optional[Tensor]]]]:
    """Helper for setting incremental state for an nn.Module."""
    if incremental_state is not None:
        result = module.set_incremental_state(incremental_state, key, value)
        if result is not None:
            incremental_state = result
    return incremental_state