@app.route('/expense/<string:wkex_id>/<int:ex_id>/update', methods=['GET', 'POST'])
@login_required
def update_expense(wkex_id, ex_id):
    name = current_user.username
    expenses = db.session.query(UserExpense).get_or_404(ex_id)
    if expenses.expensedate != current_user:
        abort(403)
    form = NewExpense()
    if form.validate_on_submit():
        expenses.category = form.category.data
        expenses.description = form.description.data
        expenses.expense = form.expense.data
        db.session.commit()
        flash('Expense updated', 'success')
        return redirect(url_for('overview'))
    elif request.method == 'GET':
        form.category.data = expenses.category
        form.description.data = expenses.description
        form.expense.data = expenses.expense
    return render_template('expenses.html', title='Expenses', form=form, name=name, wkex_id=wkex_id, state='today')