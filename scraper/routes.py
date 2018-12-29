from flask import render_template, url_for, flash, redirect
from scraper.forms import RegistrationForm, LoginForm
from scraper.models import Totals, Watchlist

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
    return  render_template('home.html', title='Home', data=data)


@app.route("/about")
def about():
    return render_template('about.html', title='About')    

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
