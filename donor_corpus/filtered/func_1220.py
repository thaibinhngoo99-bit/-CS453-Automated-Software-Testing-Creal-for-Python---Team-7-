@app.route('/filecoin-wallets')
@login_required
def filecoin_wallets():
    """
    Retrieve all wallets from all FFSes and save them in a list for
    presentation on the UI template
    """
    powergate = PowerGateClient(app.config['POWERGATE_ADDRESS'])
    try:
        ffs = Ffs.query.filter_by(user_id=current_user.id).one()
    except:
        flash('No wallets created yet.', 'alert-danger')
        return render_template('filecoin/filecoin-wallets.html', wallets=None, breadcrumb='Filecoin / Wallets')
    wallets = []
    addresses = powergate.ffs.addrs_list(ffs.token)
    for address in addresses.addrs:
        balance = powergate.wallet.balance(address.addr)
        wallets.append({'ffs': ffs.ffs_id, 'name': address.name, 'address': address.addr, 'type': address.type, 'balance': str(balance.balance)})
    return render_template('filecoin/filecoin-wallets.html', wallets=wallets, breadcrumb='Filecoin / Wallets')