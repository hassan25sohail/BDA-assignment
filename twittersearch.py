import tweepy
import csv
import textblob
import re
import sys
from geopy.geocoders import Nominatim
#Twitter API credentials
consumer_key = "OPqUuczeEDIru4xhGLWEyxH8K"
consumer_secret = "51DhaALID5i15iAjpjkGgs3gEz4RRgdaMa87qvCeMJTRnFGJp3"
access_key = "329938692-kLYqjEhSkMGc0XdvsSiHbjvmF5ZHUWNe2sVDaXa3"
access_secret = "RnzHc8uJl9Lu55Eu42x21VPBZsmZJBSjisThLbpYpQU70"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
geolocator = Nominatim()
location= geolocator.geocode("khi")
print(location.latitude)
location=str(location.latitude)+","+str(location.longitude)
for tweet in tweepy.Cursor(api.search,
                           q=["iphone"],
                           rpp=100,
                           result_type="recent",
                           pages=5000,
                           geocode=location+",8km",
                           include_entities=False,
                           lang="en").items(5000):
    #re tweet ak hi bar show hon
    if (not tweet.retweeted) and ('RT @' not in tweet.text):

        s=[]
        text=tweet.text

        analysis=textblob.TextBlob(text).sentiment.polarity

        print( text)
