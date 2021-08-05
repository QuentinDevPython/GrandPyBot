from .. import api_google_maps as script
from .config import GOOGLE_MAP_KEY

import urllib.request

def test_http_result(monkeypatch):
    results = [
        2.2944813, 
        48.85837009999999, 
        'Champ de Mars, 5 Av. Anatole France, 75007 Paris, France'
    ]

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    assert script.ApiGoogleMaps(GOOGLE_MAP_KEY).get_coords_place("tour eiffel paris") == results