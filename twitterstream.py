import tweepy,json,textblob,mysql
import re,time
import geocoder

class MyStreamListener(tweepy.StreamListener):
        def on_data(self, raw_data):
            json_load = json.loads(raw_data)
            text = json_load['text']
            if 'RT @' not in text:
                list=[]
                json_load = json.loads(raw_data)
                texts = json_load['text']
                usr_name=json_load['user']['screen_name']
                mentions=json_load['entities']['user_mentions']
                mentioned_users= [ mention["screen_name"] for mention in mentions ]
                hashs=json_load['entities']['hashtags']
                hash= [ hash["text"] for hash in hashs ]
                urls=json_load['entities']['urls']
                url = [ url["url"] for url in urls ]
                tweet_retweeted=json_load['retweet_count']
                tweet_createdat=json_load['created_at']
                usr_folower=json_load['user']['followers_count']
                analysis=textblob.TextBlob(texts).sentiment.polarity

                list=[usr_name,text,mentioned_users,hash,url,usr_folower,analysis,tweet_retweeted,tweet_createdat]
                print(list)
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

    def tweets(self,keyword,loc):
            stringx=[]
            self.keyword=keyword
            self.location=loc
            myStreamListener = MyStreamListener()
            myStream = tweepy.Stream(auth = self.api.auth, listener=myStreamListener)
            g = geocoder.google(loc)
            location=g.geojson['bbox']
            self.stringx=[]
            x=myStream.filter(locations=[location[0],location[1],location[2],location[3]],languages=["en"],track=[keyword],async=True)
            time.sleep(10)
            myStream.disconnect()
           # return True


insertTweets().tweets("car","India")

