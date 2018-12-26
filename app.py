# set environment variables: export FLASK_APP=app.py
# set environment variables: export FLASK_DEBUG=1
# flask run


from flask import Flask, render_template
app = Flask(__name__)


# two routes being handled by the same function
@app.route("/")
@app.route("/home")
def home():
    return  render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')    

# this only needed to run directly using python prompt >>>
# set FLASK_APP=app
# set FLASK_DEBUG=true
# python -m flask run --port 3000
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=3000)

