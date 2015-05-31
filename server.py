"""House Hunter""" 

import os, rauth, json, requests, pprint, time, argparse

from jinja2 import StrictUndefined
from yelpapi import YelpAPI
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import Home, connect_to_db, db


app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage (where user will select city)"""

    return render_template("homepage.html")

@app.route('/get_homes')
def map():
#     """Return map_page html with correct map on it"""
#     """QUERY THE DATABASE FOR THE HOMES IN THAT CITY"""
    city_id = request.args.get('city_id')
    print city_id
    return render_template("map_page.html")
#     city_id = request.args.get('city_id')

#     listings = Home.query.filter_by(city_id=city_id).all()
#     print "THIS WORKS"
    
#     # listing_data = json.loads(request.text)

# @app.route("/city")
# def get_city:
#     """Gets the city selected by the user on the landing page"""

#     city = request.  (city image ID?)
#     houses = Homes.query.filter_by(city=city).all()

#     return jsonify(homes query variables and send them over)




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.run(debug=True)

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()