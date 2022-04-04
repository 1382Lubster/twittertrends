
import tweepy
import os
import json
import sys
import geocoder

# API Keys and Tokens
# Authenticate
consumer_key= 'qeUQeUh0W7eieUcOXyw1VKa7X'
consumer_secret= 'xOozxD6HoryZBEFfJdH1PjNNK5NuApsZOdTalthBVPA3L1xb6I'
access_token= '1276930174328717312-qxyEaWjEbyM1udUNUam9sMNxkZNWro'
access_token_secret= 'mB9Td9HrpS4wjGeefwLYoHMQaDJFUYjUGyJ0QpKSSqG4e'

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