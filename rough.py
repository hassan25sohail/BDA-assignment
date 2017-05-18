from twython import TwythonStreamer
from geopy.geocoders import Nominatim
consumer_key = "OPqUuczeEDIru4xhGLWEyxH8K"
consumer_secret = "51DhaALID5i15iAjpjkGgs3gEz4RRgdaMa87qvCeMJTRnFGJp3"
access_key = "329938692-kLYqjEhSkMGc0XdvsSiHbjvmF5ZHUWNe2sVDaXa3"
access_secret = "RnzHc8uJl9Lu55Eu42x21VPBZsmZJBSjisThLbpYpQU70"
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text']

    def on_error(self, status_code, data):
        print status_code
geolocator = Nominatim()
location= geolocator.geocode("usa")
stream = MyStreamer(consumer_key, consumer_secret,
                    access_key, access_secret)
stream.statuses.filter(track='car',locations=[location.latitude,location.longitude,location.latitude+1,location.longitude-1])

