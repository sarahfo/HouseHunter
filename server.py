"""House Hunter""" 

import os, rauth, json, requests, pprint, time, argparse

from jinja2 import StrictUndefined
from yelpapi import YelpAPI
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import Home, User, connect_to_db, db


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
    setView = {}
    if city_id == "SD":
        setView['lat'] =  32.732996
        setView['lon'] =  117.163868
    # elif city_id == "Port":
    #     setView.update[{'lat':45.523062, 'lon':-122.676482}]
    # elif city_id == "SF":
    #     setView.update[{'lat': 37.766237, 'lon':-122.439280}]
    # elif city_id == "DC":
    #     setView.update[{'lat': 38.900652, 'lon':-77.030897}]
    # elif city_id == "SEA":
    #     setView.update[{'lat': 47.606209, 'lon':-122.332071}]
    else:
        print "no city id selected"
    setView = setView
    
     #gets the data value passed in URL to key city_id
    print setView
    # listings = Home.query.filter(Home.city_id == city_id).first()
    # print listings
    # listings = json.loads(request.text)
    # EITHER PARSE JSON HERE OR SEND IT BACK TO SCRIPT FOR JINJA TO DEAL WITH.
    # FOR MAPPING OBJECTS, need the address or lat/lon. 
    return render_template("map_page.html", setView=setView)

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