import googlemaps

class ApiGoogleMaps:

    def __init__(self,GOOGLE_MAP_KEY):
        self.gmaps = googlemaps.Client(key=GOOGLE_MAP_KEY)

    def get_coords_place(self,place):
        geocode_result = self.gmaps.geocode(place)
        if len(geocode_result) > 0:
            return [geocode_result[0]["geometry"]["location"]["lng"], 
                    geocode_result[0]["geometry"]["location"]["lat"],
                    geocode_result[0]["formatted_address"]]
