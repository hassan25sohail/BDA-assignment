import tweepy,json,textblob,mysql
import re,time
from geopy.geocoders import Nominatim

class helper :
    def remove_emoji(self,data):
        if not data:
            return data
        if not isinstance(data, basestring):
            return data
        try:
            patt = self.re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        except self.re.error:
            patt = self.re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
        return patt.sub('', data)

    def remove_link(self,data):
        return self.re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '',data, flags=self.re.MULTILINE)

class MyStreamListener(tweepy.StreamListener):
        def on_data(self, raw_data):
            #if not raw_data.retweeted:
                json_load = json.loads(raw_data)
                texts = json_load['text']
                coded = texts.encode('utf-8')
                s = str(coded)
                tweet=s[0:-1]
                analysis=textblob.TextBlob(texts).sentiment
                #print(texts+"::"+str(analysis))
                print("cool")

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
            geolocator = Nominatim()
            location= geolocator.geocode(location)
            print location.raw['lon']
            #geocode=str(location.latitude)+","+str(location.longitude)+","+str(location.latitude-1)+","+str(location.longitude+1)
            x=myStream.filter(locations=[location.latitude,location.longitude,location.latitude+1,location.longitude-1])
            print x

insertTweets().tweets("car","India")
