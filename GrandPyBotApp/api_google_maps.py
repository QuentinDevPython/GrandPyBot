import googlemaps
import json

class ApiGoogleMaps:

    def __init__(self, place):
        self.gmaps = googlemaps.Client(key="AIzaSyAOfNay0_N9OeJ1ScvGN4cqx8DIIS9Ib_M")
        self.requested_place = [place] #Récupérer le lieu demandé par l'utilisateur

    def get_coords_place(self):
        with open('place.json', 'w') as json_file:
            for place in self.requested_place:
                geocode_result = self.gmaps.geocode(place)
                if len(geocode_result) > 0:
                    json.dump(
                            [place, 
                            geocode_result[0]["geometry"]["location"]["lng"], 
                            geocode_result[0]["geometry"]["location"]["lat"]
                            ],
                        json_file
                    )




