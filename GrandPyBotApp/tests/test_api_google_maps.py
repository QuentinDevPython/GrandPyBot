from .. import api_google_maps as script

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

    assert script.ApiGoogleMaps("AIzaSyAqgvq_H95ho3m5U4M_mjeErXXJ5cPxhwg").get_coords_place("tour eiffel france") == results