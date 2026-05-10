@app.route('/expense/<string:day_id>/charts', methods=['GET', 'POST'])
@login_required
def charts(day_id):
    userids = current_user.id
    name = current_user.username
    categories = db.session.query(UserExpense.category).filter(UserExpense.userid == userids, UserExpense.expense_date == day_id).distinct()
    cat_list = []
    for u in categories:
        cat_list.append(f'{u.category}')
    counts_list = []
    for item in cat_list:
        counts = db.session.query(UserExpense.category).filter(UserExpense.userid == userids, UserExpense.expense_date == day_id, UserExpense.category == item).count()
        counts_list.append(counts)
    sum_list = []
    for item in cat_list:
        Sums = db.session.query(func.sum(UserExpense.expense)).filter(UserExpense.userid == userids, UserExpense.expense_date == day_id, UserExpense.category == item).scalar()
        sum_list.append(f'{Sums}')
    fig, axs = plt.subplots(figsize=(10, 5))
    axs.bar(cat_list, [float(g) for g in sum_list])
    fig.suptitle('Expenditure breakdown')
    fig1, ax1 = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect='equal'))
    wedges, texts = ax1.pie(counts_list, wedgeprops=dict(width=0.5), startangle=-40)
    bbox_props = dict(boxstyle='square,pad=0.3', fc='w', ec='k', lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle='-'), bbox=bbox_props, zorder=0, va='top')
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: 'right', 1: 'left'}[int(np.sign(x))]
        connectionstyle = 'angle,angleA=0,angleB={}'.format(ang)
        kw['arrowprops'].update({'connectionstyle': connectionstyle})
        ax1.annotate(cat_list[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y), horizontalalignment=horizontalalignment, **kw)
    ax1.set_title('Expenses category frequency')
    highpngImage = io.BytesIO()
    freqpngImage = io.BytesIO()
    FigureCanvas(fig).print_png(highpngImage)
    FigureCanvas(fig1).print_png(freqpngImage)
    highpngImageString = 'data:image/png;base64,'
    highpngImageString += base64.b64encode(highpngImage.getvalue()).decode('utf8')
    freqpngImageString = 'data:image/png;base64,'
    freqpngImageString += base64.b64encode(freqpngImage.getvalue()).decode('utf8')
    return render_template('charts.html', title='History', name=name, image1=highpngImageString, image2=freqpngImageString, day_id=day_id)
    if __name__ == '__main__':
        app.run()