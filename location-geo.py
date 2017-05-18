from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("gulshan karachi,pk")
print(location.address)
print((location.latitude, location.longitude))
