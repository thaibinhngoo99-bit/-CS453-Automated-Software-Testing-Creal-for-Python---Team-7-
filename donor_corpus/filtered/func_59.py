@app.route('/', methods=['GET', 'POST'])
def login():
    form = UserLogin()
    if current_user.is_authenticated:
        return redirect(url_for('overview'))
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('overview'))
        else:
            flash('Invalid login', 'danger')
    return render_template('login.html', form=form)