from flask import Flask, render_template, redirect, url_for, flash, request, abort
from functions import UserLogin, UserRegistration, NewExpense
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime, timedelta, date
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from itertools import zip_longest
import os
import io
import base64
import numpy as np

app = Flask(__name__)
SECRET_KEY = os.urandom(16)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = ' '
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    expense_id = db.relationship('UserExpense', backref='expensedate', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class UserExpense(db.Model):
    __tablename__ = 'user_expenses'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(30))
    description = db.Column(db.String(50))
    expense = db.Column(db.Numeric(scale=2, asdecimal=True))
    expense_date = db.Column(db.Date, default=date.today())

    def __repr__(self):
        return f"UserExpense('{self.category}', '{self.description}', '{self.expense}', '{self.expense_date}')"

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('overview'))
    form = UserRegistration()
    if form.validate_on_submit():
        password_hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=password_hashed)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out!', 'success')
    return redirect(url_for('login'))

@app.route('/overview', methods=['GET','POST'])
@login_required
def overview():
    form = NewExpense()
    userids = current_user.id
    name = current_user.username

    # Forms
    if form.validate_on_submit():
        expenses = UserExpense(category=form.category.data, description=form.description.data,
                                expense=form.expense.data, expensedate=current_user)
        db.session.add(expenses)
        db.session.commit()

    # Queries
    filters = db.session.query(UserExpense.expense_date).filter(UserExpense.userid==userids).distinct()

    date_list=[] #List of distinct dates
    for u in filters:
        date_list.append(f'{u.expense_date}')

    date_expense_list=[] #List of expenses for that specific date
    for item in date_list:
        date_expense = db.session.query(func.sum(UserExpense.expense)).filter(UserExpense.userid==userids, UserExpense.expense_date==item).scalar()
        date_expense_list.append(f'{date_expense}')

    item = list(zip_longest(date_list,date_expense_list,date_list, fillvalue=""))

    # Matplotlib
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(date_list, [float(g) for g in date_expense_list], label="Expenses")
    ax.legend()
    fig.suptitle('Expense pattern')

    patternpngImage = io.BytesIO()
    FigureCanvas(fig).print_png(patternpngImage)

    patternpngImageString = "data:image/png;base64,"
    patternpngImageString += base64.b64encode(patternpngImage.getvalue()).decode('utf8')


    return render_template('overview.html', normal='normal', title='Expenses',image=patternpngImageString,
                           form=form, name=name, item=item)


@app.route('/expense/<string:wkex_id>', methods=['GET','POST'])
@login_required
def userexpenses(wkex_id):
    form = NewExpense()
    userids = current_user.id
    name = current_user.username

    # Queries
    items = db.session.query(UserExpense).filter(UserExpense.userid==userids, UserExpense.expense_date==wkex_id)

    todays = str(date.today())
    state="not"
    if (wkex_id == todays) is True:
        state="today"
    if (wkex_id > todays) is True:
        abort(404)

    # Forms
    if form.validate_on_submit():
        expenses = UserExpense(category=form.category.data, description=form.description.data,
                                expense=form.expense.data, expensedate=current_user)
        db.session.add(expenses)
        db.session.commit()
        flash('Expense added!', 'success')
        return redirect(url_for('userexpenses', wkex_id=wkex_id))

    return render_template('expenses.html', normal='normal', title='Expenses',
                           form=form, items=items, name=name, ids=wkex_id, state=state)

@app.route('/expense/<string:wkex_id>/<int:ex_id>/delete', methods=['GET','POST'])
@login_required
def delete_expense(wkex_id, ex_id):
    expenses = db.session.query(UserExpense).get_or_404(ex_id) # Query for valid access
    if expenses.expensedate != current_user:
        abort(403)
    db.session.delete(expenses)
    db.session.commit()
    flash('Expense deleted', 'success')
    return redirect(url_for('overview'))

@app.route("/expense/<string:wkex_id>/<int:ex_id>/update", methods=['GET', 'POST'])
@login_required
def update_expense(wkex_id, ex_id):
    name = current_user.username
    expenses = db.session.query(UserExpense).get_or_404(ex_id) # Query for valid access
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

    elif request.method=='GET':
        form.category.data = expenses.category
        form.description.data =expenses.description
        form.expense.data = expenses.expense
    return render_template('expenses.html', title='Expenses',form=form, name=name, wkex_id=wkex_id, state='today')

@app.route("/expense/<string:day_id>/charts", methods=['GET', 'POST'])
@login_required
def charts(day_id):
    userids = current_user.id
    name = current_user.username
    # Queries
    categories = db.session.query(UserExpense.category).filter(UserExpense.userid==userids,
                                                               UserExpense.expense_date==day_id).distinct()
    cat_list=[]
    for u in categories:
        cat_list.append(f'{u.category}')

    counts_list=[]
    for item in cat_list:
        counts = db.session.query(UserExpense.category).filter(UserExpense.userid==userids,
                                                               UserExpense.expense_date==day_id,
                                                               UserExpense.category==item).count()
        counts_list.append(counts)

    sum_list=[]
    for item in cat_list:
        Sums = db.session.query(func.sum(UserExpense.expense)).filter(UserExpense.userid==userids,
                                                                      UserExpense.expense_date==day_id,
                                                                      UserExpense.category==item).scalar()
        sum_list.append(f'{Sums}')

    # Highest expenditure graph
    fig, axs = plt.subplots(figsize=(10, 5))
    axs.bar(cat_list, [float(g) for g in sum_list])
    fig.suptitle('Expenditure breakdown')

    # Frequency graph
    fig1, ax1 = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))

    wedges, texts = ax1.pie(counts_list, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="top")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax1.annotate(cat_list[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax1.set_title("Expenses category frequency")

    # Convert plot to PNG image
    highpngImage = io.BytesIO()
    freqpngImage = io.BytesIO()
    FigureCanvas(fig).print_png(highpngImage)
    FigureCanvas(fig1).print_png(freqpngImage)

    # Encode PNG image to base64 string
    highpngImageString = "data:image/png;base64,"
    highpngImageString += base64.b64encode(highpngImage.getvalue()).decode('utf8')

    freqpngImageString = "data:image/png;base64,"
    freqpngImageString += base64.b64encode(freqpngImage.getvalue()).decode('utf8')

    return render_template('charts.html',title ='History', name=name,
                           image1=highpngImageString, image2=freqpngImageString, day_id=day_id)

    if __name__ == '__main__':
        app.run()
