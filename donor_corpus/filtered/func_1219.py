@app.route('/filecoin-download/<cid>', methods=['GET'])
@login_required
def filecoin_download(cid):
    """
    Retrieve a file from Filecoin via IPFS using Powergate and offer the user
    the option to save it to their machine.
    """
    file = Files.query.filter_by(CID=cid, user_id=current_user.id).first()
    ffs = Ffs.query.get(file.ffs_id)
    try:
        powergate = PowerGateClient(app.config['POWERGATE_ADDRESS'])
        data_ = powergate.ffs.get(file.CID, ffs.token)
        user_data = app.config['USER_DATA_DIR']
        if not os.path.exists(user_data):
            os.makedirs(user_data)
        print(user_data)
        user_dir = os.path.join(user_data, str(current_user.id) + '-' + current_user.username)
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        print(user_dir)
        filecoin_dir = os.path.join(user_dir, 'filecoin/downloads')
        if not os.path.exists(filecoin_dir):
            os.makedirs(filecoin_dir)
        print(filecoin_dir)
        with open(os.path.join(filecoin_dir, file.file_name), 'wb') as out_file:
            for data in data_:
                out_file.write(data)
        safe_path = safe_join('../' + filecoin_dir, file.file_name)
        print(safe_path)
        return send_file(safe_path, as_attachment=True)
    except Exception as e:
        flash("failed to download '{}' from Filecoin. {}".format(file.file_name, e), 'alert-danger')
        event = Logs(timestamp=datetime.now().replace(microsecond=0), event='Download ERROR: ' + file.file_name + ' CID: ' + file.CID + ' ' + str(e), user_id=current_user.id)
        db.session.add(event)
        db.session.commit()
    files = Files.query.filter_by(user_id=current_user.id).all()
    return render_template('filecoin/filecoin-files.html', files=files, breadcrumb='Filecoin / Files')