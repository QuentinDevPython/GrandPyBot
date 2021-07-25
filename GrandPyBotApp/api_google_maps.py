import googlemaps

class ApiGoogleMaps:

    def __init__(self, place):
        self.gmaps = googlemaps.Client(key="AIzaSyAqgvq_H95ho3m5U4M_mjeErXXJ5cPxhwg")
        self.place = place

    def get_coords_place(self):
        geocode_result = self.gmaps.geocode(self.place)
        if len(geocode_result) > 0:
            print(geocode_result[0]["formatted_address"])
            return [geocode_result[0]["geometry"]["location"]["lng"], 
                    geocode_result[0]["geometry"]["location"]["lat"],
                    geocode_result[0]["formatted_address"]]
