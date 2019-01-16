from flask import render_template, url_for, flash, redirect, request
from scraper import app, db, mdb, collection
from scraper.forms import RegistrationForm, LoginForm
from scraper.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, logout_user, login_required

# two routes being handled by the same function
@app.route("/")
@app.route("/home")
def home():
    try:
        data = collection.find()
        return  render_template('home.html', title='Home', data=data)
    except Exception as e:
        # TODO: make a good informative error page
        return render_template('about.html', title='About')


@app.route("/about")
def about():
    return render_template('about.html', title='About')    


@app.route("/register", methods=['GET','POST'])
def register():
    users = User.query.all()
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
    users = User.query.all()
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
