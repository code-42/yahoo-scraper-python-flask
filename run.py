# source youtube video https://www.youtube.com/watch?v=MwZwr5Tvyxo

# set environment variables: export FLASK_APP=app.py
# set environment variables: export FLASK_DEBUG=1

from scraper import app

# this only needed to run directly using python prompt >>>
# set FLASK_APP=app
# set FLASK_DEBUG=true
# python -m flask run --port 3000
if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=3000)
    app.run(debug=True)
