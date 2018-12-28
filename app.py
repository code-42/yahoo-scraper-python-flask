# set environment variables: export FLASK_APP=app.py
# set environment variables: export FLASK_DEBUG=1
# flask run

# video 4 https://www.youtube.com/watch?v=cYWiDiIUxQc

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xf1\\3\x91p\x97i>\x9a\xeal\x1e\xe2\xcc\xd3y"\x96\xfca\xb7\xf6`\xa7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# sqlite database for scraped data
class Totals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todaysDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    currentMarketValue = db.Column(db.String(20))
    dayGain = db.Column(db.String(20))
    totalGain = db.Column(db.String(20))
    watchlist = db.relationship('Watchlist', backref='login-username', lazy=True)
    # see video 4 @ 16:50 for explanation of db.relationship and backref

    def __repr__(self):
        return f"Totals( \
            '{self.todaysDate}', \
            '{self.currentMarketValue}', \
            '{self.dayGain}', \
            '{self.totalGain}' \
            )"

class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todaysDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    symbol = db.Column(db.String(20), nullable=False)
    lastPrice = db.Column(db.String(20))
    todaysChange = db.Column(db.String(20))
    percentChange = db.Column(db.String(20))
    currency = db.Column(db.String(20))
    marketTime = db.Column(db.String(20))
    volume = db.Column(db.String(20))
    shares = db.Column(db.String(20))
    avgVol = db.Column(db.String(20))
    dayRange = db.Column(db.String(20))
    fiftyTwoWkRange = db.Column(db.String(20))
    dayChart = db.Column(db.String(20))
    marketCap = db.Column(db.String(20))
    totals_id = db.Column(db.Integer, db.ForeignKey('totals.id'), nullable=False)
    # see video 4 @ 16:50 for explanation of totals_id and ForeignKey  

    def __repr__(self):
        return f"Watchlist( \
            '{self.todaysDate}', \
            '{self.symbol}', \
            '{self.lastPrice}', \
            '{self.todaysChange}', \
            '{self.percentChange}', \
            '{self.currency}', \
            '{self.marketTime}', \
            '{self.volume}', \
            '{self.shares}', \
            '{self.avgVol}', \
            '{self.dayRange}', \
            '{self.fiftyTwoWkRange}', \
            '{self.dayChart}', \
            '{self.marketCap}' \
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

