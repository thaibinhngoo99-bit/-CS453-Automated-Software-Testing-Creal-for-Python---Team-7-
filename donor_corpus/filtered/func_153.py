def get_loss_at_strike(strike: float, chain: pd.DataFrame) -> float:
    """Function to get the loss at the given expiry

    Parameters
    ----------
    strike: Union[int,float]
        Value to calculate total loss at
    chain: Dataframe:
        Dataframe containing at least strike and openInterest

    Returns
    -------
    loss: Union[float,int]
        Total loss
    """
    itm_calls = chain[chain.index < strike][['OI_call']]
    itm_calls['loss'] = (strike - itm_calls.index) * itm_calls['OI_call']
    call_loss = itm_calls['loss'].sum()
    itm_puts = chain[chain.index > strike][['OI_put']]
    itm_puts['loss'] = (itm_puts.index - strike) * itm_puts['OI_put']
    put_loss = itm_puts.loss.sum()
    loss = call_loss + put_loss
    return loss