@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out!', 'success')
    return redirect(url_for('login'))