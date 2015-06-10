"""House Hunter""" 

import os, rauth, json, requests, pprint, time, argparse

from jinja2 import StrictUndefined
from yelpapi import YelpAPI
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import House, User, connect_to_db, db
from sqlalchemy import func


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
        setView['lon'] = -117.163868
        city="San Diego, CA"
    elif city_id == "PORT":
        setView['lat'] = 45.523062
        setView['lon'] = -122.676482
        city="Portland, OR"
    elif city_id == "SF":
        setView['lat'] = 37.766237
        setView['lon'] = -122.439280
        city="San Francisco, CA"
    elif city_id == "DC":
        setView['lat'] = 38.900652
        setView['lon'] = -77.030897
        city="Washington, DC"
    elif city_id == "SEA":
        setView['lat'] = 47.606209
        setView['lon'] = -122.332071
        city="Seattle, WA"
    else:
        print "no city id selected"

    listings = House.query.filter_by(city_id=city_id).all()
    min_max_price = db.session.query(db.func.min(House.list_price), db.func.max(House.list_price)).filter_by(city_id=city_id).one()
    print setView

    return render_template("map_page.html", setView=setView, listings=listings, city=city, min_max_price=min_max_price)

@app.route('/yelp_params', methods=['GET'])
def search_parameters():
    """Gets the list of user-selected categories and location and sends them to Yelp API"""
    if request.args:
        yelp_search_selection = request.args.getlist('category_filter')
        yelp_search = ",".join(yelp_search_selection)
        yelp_location = request.args['location']
        
        businesses = get_results(make_parameters(yelp_search, yelp_location))
        return jsonify(businesses=businesses)
        
def make_parameters(yelp_search, yelp_location):
    """Yelp API defines the key names for the parameters."""
    params = {}
    params['category_filter'] = yelp_search
    params ["location"] = yelp_location
    print params

    return params

def get_results(params):
    """OAuth Session with secret keys, sourced from OS."""
    
    auth_session = rauth.OAuth1Session(
        consumer_key = os.environ['YELP_CONSUMER_KEY'],
        consumer_secret = os.environ['YELP_CONSUMER_SECRET'],
        access_token = os.environ['YELP_ACCESS_TOKEN_KEY'],
        access_token_secret = os.environ['YELP_ACCESS_TOKEN_SECRET'])

    request = auth_session.get("http://api.yelp.com/v2/search", params=params)   
   
    data = json.loads(request.text)  #Transforms the JSON API response into a Python dictionary
    auth_session.close()
    
    businesses = data['businesses']
    pprint.pprint(data)
    # print businesses
    return businesses


@app.errorhandler(404)
def fourOhFour(error):
   return render_template("fourohfour.html"), 404
        

if __name__ == "__main__":
    connect_to_db(app)
    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(debug=False)
