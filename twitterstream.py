import tweepy,json,textblob,MySQLdb,mysqlconn
import time
import geocoder
import  MySQLdb


class MyStreamListener(tweepy.StreamListener):
        keyword,location='',''
        def setuserpram(self,keyword,location):
            self.keyword=keyword
            self.location=location

        def on_data(self, raw_data):
            raw_data.encode("utf-8")
            json_load = json.loads(raw_data)
            text = json_load['text']
            if 'RT @' not in text:
                db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="ironhorse100",  # your password
                     db="zain")        # name of the data base
                list=[]
                json_load = json.loads(raw_data)
                texts = json_load['text']
                text=text.replace("'", "")
                usr_name=json_load['user']['screen_name']
                mentions=json_load['entities']['user_mentions']
                mentioned_users=  ",".join(str(mention["screen_name"] )for mention in mentions )
                hashs=json_load['entities']['hashtags']
                hash=  ",".join(str(hash["text"] ) for hash in hashs )
                urls=json_load['entities']['urls']
                url = ",".join(str(url["url"] )for url in urls )
                tweet_retweeted=json_load['retweet_count']
                tweet_createdat=json_load['created_at']
                usr_folower=json_load['user']['followers_count']
                analysis=textblob.TextBlob(texts).sentiment.polarity

                list=[usr_name,text,mentioned_users,hash,url,usr_folower,analysis,tweet_retweeted,tweet_createdat,self.keyword,self.location]
                cur = db.cursor()
                sql="INSERT INTO `tweets` (`user`, `tweet`,`mentions`, `hashtags`, `urls`,`followers`, `retweet`, `createdat`, `keyword`, `location`) VALUES ('{}','\{}\','{}','{}','{}',{},{},{},'{}','{}');"\
                    .format(list[0],list[1].encode('ascii', 'ignore').decode('ascii'),
                            list[2],list[3],list[4],list[5],list[6]
                            ,list[7],list[8],list[9])
                y=cur.execute(sql)
                db.commit()
                print(sql)
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
            myStreamListener = MyStreamListener()
            myStreamListener.setuserpram(keyword,loc)
            myStream = tweepy.Stream(auth = self.api.auth, listener=myStreamListener)
            g = geocoder.google(loc)
            location=g.geojson['bbox']
            self.stringx=[]
            x=myStream.filter(locations=[location[0],location[1],location[2],location[3]],languages=["en"],track=[keyword],async=True,encoding='utf-8')
            time.sleep(10)
            myStream.disconnect()
           # return True


insertTweets().tweets("car","Pakistan")

