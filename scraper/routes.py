from flask import render_template, url_for, flash, redirect, request
from scraper import app, db
from scraper.forms import RegistrationForm, LoginForm
from scraper.models import Totals, Watchlist, User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, logout_user, login_required


# dummy data for scraper
data = [
    {
        'market_time': '2018-12-26 10:40 AM',
        'current_market_value': '$22169.90',
        'todays_gain': '$292.90',
        'total_gain': '$7996.20'
    },
    {
        'market_time': '2018-12-26 10:50 AM',
        'current_market_value': '$22240.40',
        'todays_gain': '$372.90',
        'total_gain': '$8066.70'
    }
]

# two routes being handled by the same function
@app.route("/")
@app.route("/home")
def home():
    users = User.query.all()
    return  render_template('home.html', title='Home', data=data, users=users)


@app.route("/about")
def about():
    return render_template('about.html', title='About')    


@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    users = User.query.all()
    form = RegistrationForm()
    if form.validate_on_submit():
        # source https://docs.python.org/2/library/hashlib.html
        hashed_password = generate_password_hash(form.password.data)
        print(hashed_password)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form, users=users)


@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    users = User.query.all()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # get() method returns none if next parameter doesnot exist
            # square brackets [key_name] would throw an error
            # next parameter is optional
            next_page = request.args.get('next')
            # ternary conditional of the form ? yes:no
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form, users=users)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
