import tweepy,json,textblob,mysql
import re,time
import geocoder

class MyStreamListener(tweepy.StreamListener):
        def on_data(self, raw_data):
                json_load = json.loads(raw_data)
                texts = json_load['text']
                usr=json_load['user']
                analysis=textblob.TextBlob(texts).sentiment
                #print(texts+"::"+str(analysis))
                print(usr)

                return True

        def on_status(self, status):
            return status.text

class insertTweets:
    #Twitter API credentials
    def __init__(self):
        _consumer_key ,_consumer_secret = "OPqUuczeEDIru4xhGLWEyxH8K","51DhaALID5i15iAjpjkGgs3gEz4RRgdaMa87qvCeMJTRnFGJp3"
        _access_key,_access_secret = "329938692-kLYqjEhSkMGc0XdvsSiHbjvmF5ZHUWNe2sVDaXa3", "RnzHc8uJl9Lu55Eu42x21VPBZsmZJBSjisThLbpYpQU70"
        auth = tweepy.OAuthHandler(_consumer_key, _consumer_secret)
        auth.set_access_token(_access_key, _access_secret)
        self.api = tweepy.API(auth)

    def tweets(self,keyword,location):
            myStreamListener = MyStreamListener()
            myStream = tweepy.Stream(auth = self.api.auth, listener=myStreamListener)
            g = geocoder.google(location)
            location=g.geojson['bbox']
            x=myStream.filter(locations=[location[0],location[1],location[2],location[3]],languages=["en"],track=[keyword])
            print x

insertTweets().tweets("car","India")
