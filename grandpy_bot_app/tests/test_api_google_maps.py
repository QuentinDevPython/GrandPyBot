"""Import the module urllib.request to open URLs (HTTP)
in a complex world.
Import also the file which is going to be tested (api_google_maps)
and the Google Map Key to simulate the connexion with Google Maps."""
import urllib.request

from .config import GOOGLE_MAP_KEY
from .. import api_google_maps as script


def test_http_result(monkeypatch):
    """
    Method which compares the expected results of the API function
    with the results obtained by this simulation
    """

    results = [
        2.2944813,
        48.85837009999999,
        'Champ de Mars, 5 Av. Anatole France, 75007 Paris, France'
    ]

    def mockreturn():
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    assert script.ApiGoogleMaps(GOOGLE_MAP_KEY).get_coords_place(
        "tour eiffel paris") == results
