@app.route('/expense/<string:wkex_id>', methods=['GET', 'POST'])
@login_required
def userexpenses(wkex_id):
    form = NewExpense()
    userids = current_user.id
    name = current_user.username
    items = db.session.query(UserExpense).filter(UserExpense.userid == userids, UserExpense.expense_date == wkex_id)
    todays = str(date.today())
    state = 'not'
    if (wkex_id == todays) is True:
        state = 'today'
    if (wkex_id > todays) is True:
        abort(404)
    if form.validate_on_submit():
        expenses = UserExpense(category=form.category.data, description=form.description.data, expense=form.expense.data, expensedate=current_user)
        db.session.add(expenses)
        db.session.commit()
        flash('Expense added!', 'success')
        return redirect(url_for('userexpenses', wkex_id=wkex_id))
    return render_template('expenses.html', normal='normal', title='Expenses', form=form, items=items, name=name, ids=wkex_id, state=state)