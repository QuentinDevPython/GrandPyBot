from api_google_maps import ApiGoogleMaps

string = "tour eiffel"
map = ApiGoogleMaps(string)
map.get_coords_place()
