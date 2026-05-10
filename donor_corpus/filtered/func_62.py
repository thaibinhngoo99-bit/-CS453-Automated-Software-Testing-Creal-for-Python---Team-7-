@app.route('/overview', methods=['GET', 'POST'])
@login_required
def overview():
    form = NewExpense()
    userids = current_user.id
    name = current_user.username
    if form.validate_on_submit():
        expenses = UserExpense(category=form.category.data, description=form.description.data, expense=form.expense.data, expensedate=current_user)
        db.session.add(expenses)
        db.session.commit()
    filters = db.session.query(UserExpense.expense_date).filter(UserExpense.userid == userids).distinct()
    date_list = []
    for u in filters:
        date_list.append(f'{u.expense_date}')
    date_expense_list = []
    for item in date_list:
        date_expense = db.session.query(func.sum(UserExpense.expense)).filter(UserExpense.userid == userids, UserExpense.expense_date == item).scalar()
        date_expense_list.append(f'{date_expense}')
    item = list(zip_longest(date_list, date_expense_list, date_list, fillvalue=''))
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(date_list, [float(g) for g in date_expense_list], label='Expenses')
    ax.legend()
    fig.suptitle('Expense pattern')
    patternpngImage = io.BytesIO()
    FigureCanvas(fig).print_png(patternpngImage)
    patternpngImageString = 'data:image/png;base64,'
    patternpngImageString += base64.b64encode(patternpngImage.getvalue()).decode('utf8')
    return render_template('overview.html', normal='normal', title='Expenses', image=patternpngImageString, form=form, name=name, item=item)