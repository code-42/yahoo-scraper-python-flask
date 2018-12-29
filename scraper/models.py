from datetime import datetime
from flaskblog import db

# sqlite database for scraped data
class Totals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todaysDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    currentMarketValue = db.Column(db.String(20))
    dayGain = db.Column(db.String(20))
    totalGain = db.Column(db.String(20))
    watchlist = db.relationship('Watchlist', backref='login-username', lazy=True)
    # see video 4 @ 16:50 for explanation of db.relationship and backref
    # video 4 https://www.youtube.com/watch?v=cYWiDiIUxQc

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
