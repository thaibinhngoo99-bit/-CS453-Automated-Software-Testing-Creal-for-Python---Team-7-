def calculate_max_pain(chain: pd.DataFrame) -> int:
    """Returns the max pain for a given call/put dataframe

    Parameters
    ----------
    chain: DataFrame
        Dataframe to calculate value from

    Returns
    -------
    max_pain : int
        Max pain value
    """
    strikes = np.array(chain.index)
    if 'OI_call' not in chain.columns or 'OI_put' not in chain.columns:
        print('Incorrect columns.  Unable to parse max pain')
        return np.nan
    loss = []
    for price_at_exp in strikes:
        loss.append(get_loss_at_strike(price_at_exp, chain))
    chain['loss'] = loss
    max_pain = chain['loss'].idxmin()
    return max_pain