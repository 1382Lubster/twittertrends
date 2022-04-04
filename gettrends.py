
import tweepy
import os
import json
import sys
import geocoder

# API Keys and Tokens
# Authenticate
consumer_key= 'xxxxxxxx'
consumer_secret= 'xxxxxxx'
access_token= 'xxxxxxxxxxxxxxxxx'
access_token_secret= 'xxxxxxxxxxxxxxxxxx'

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Available Locations
available_loc = api.trends_available()
# writing a JSON file that has the available trends around the world
with open("available_locs_for_trend.json","w") as wp:
    wp.write(json.dumps(available_loc, indent=1))

# Trends for Specific Country
loc = sys.argv[1]     # location as argument variable 
g = geocoder.osm(loc) # getting object that has location's latitude and longitude

closest_loc = api.trends_closest(g.lat, g.lng)
trends = api.trends_place(closest_loc[0]['woeid'])
# writing a JSON file that has the latest trends for that location
with open("twitter_{}_trend.json".format(loc),"w") as wp:
    wp.write(json.dumps(trends, indent=1))