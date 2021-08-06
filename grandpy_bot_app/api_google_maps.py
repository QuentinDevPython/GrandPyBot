"""Import the module googlemaps to access to the Google Maps features."""
import googlemaps


class ApiGoogleMaps:
    """
    Class that allows to get the GPS coordinates and the address of
    a specific place.

    Args:
        gmaps (object to access Google Maps with an API_key specified)
    """

    def __init__(self, GOOGLE_MAP_KEY):
        self.gmaps = googlemaps.Client(key=GOOGLE_MAP_KEY)

    def get_coords_place(self, place):
        """
        Function that returns the GPS coordinates and the address of the place in parameter.
        """
        geocode_result = self.gmaps.geocode(place)
        if len(geocode_result) > 0:
            return [geocode_result[0]["geometry"]["location"]["lng"],
                    geocode_result[0]["geometry"]["location"]["lat"],
                    geocode_result[0]["formatted_address"]]
        return None
