@app.route('/expense/<string:wkex_id>/<int:ex_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_expense(wkex_id, ex_id):
    expenses = db.session.query(UserExpense).get_or_404(ex_id)
    if expenses.expensedate != current_user:
        abort(403)
    db.session.delete(expenses)
    db.session.commit()
    flash('Expense deleted', 'success')
    return redirect(url_for('overview'))