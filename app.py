# set environment variables: export FLASK_APP=app.py
# set environment variables: export FLASK_DEBUG=1
# flask run

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xf1\\3\x91p\x97i>\x9a\xeal\x1e\xe2\xcc\xd3y"\x96\xfca\xb7\xf6`\xa7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# sqlite database for scraped data
class Totals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todaysDate = db.Column(db.String(20), unique=True, nullable=False)
    currentMarketValue = db.Column(db.String(20), unique=True, nullable=False)
    dayGain = db.Column(db.String(20), unique=True, nullable=False)
    totalGain = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Totals('{self.todaysDate}', '{self.currentMarketValue}', '{self.dayGain}', '{self.totalGain}')"

class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todaysDate = db.Column(db.String(20), unique=True, nullable=False)
    symbol = db.Column(db.String(20), unique=True, nullable=False)
    lastPrice = db.Column(db.String(20), unique=True, nullable=False)
    todaysChange = db.Column(db.String(20), unique=True, nullable=False)
    percentChange = db.Column(db.String(20), unique=True, nullable=False)
    currency = db.Column(db.String(20), unique=True, nullable=False)
    marketTime = db.Column(db.String(20), unique=True, nullable=False)
    volume = db.Column(db.String(20), unique=True, nullable=False)
    shares = db.Column(db.String(20), unique=True, nullable=False)
    avgVol = db.Column(db.String(20), unique=True, nullable=False)
    dayRange = db.Column(db.String(20), unique=True, nullable=False)
    fiftyTwoWkRange = db.Column(db.String(20), unique=True, nullable=False)
    dayChart = db.Column(db.String(20), unique=True, nullable=False)
    marketCap = db.Column(db.String(20), unique=True, nullable=False)
    

    def __repr__(self):
        return f"Watchlist(
            '{self.todaysDate}', 
            '{self.symbol}', 
            '{self.lastPrice}', 
            '{self.todaysChange}',
            '{self.percentChange}', 
            '{self.currency}', 
            '{self.marketTime}',
            '{self.volume}', 
            '{self.shares}', 
            '{self.avgVol}',
            '{self.dayRange}',
            '{self.fiftyTwoWkRange}', 
            '{self.dayChart}', 
            '{self.marketCap}'
            )"


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


# this only needed to run directly using python prompt >>>
# set FLASK_APP=app
# set FLASK_DEBUG=true
# python -m flask run --port 3000
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=3000)

