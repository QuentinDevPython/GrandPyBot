from .. import api_wikipedia as script

import urllib.request

def test_http_result(monkeypatch):
    results = [
        'Tour Eiffel', 
        'La tour Eiffel  est une tour de fer puddlé '
        'de 324 mètres de hauteur (avec antennes) '
        'située à Paris, à l’extrémité nord-ouest '
        'du parc du Champ-de-Mars en bordure de '
        'la Seine dans le 7e arrondissement. Son '
        'adresse officielle est 5, avenue '
        'Anatole-France.\nConstruite en deux ans '
        'par Gustave Eiffel et ses collaborateurs '
        'pour l’Exposition universelle de Paris de '
        '1889, et initialement nommée « tour de 300 '
        'mètres », elle est devenue le symbole de la '
        'capitale française et un site touristique '
        'de premier plan : il s’agit du troisième '
        'site culturel français payant le plus '
        'visité en 2015, avec 5,9 millions de '
        'visiteurs en 2016.', 
        'https://fr.wikipedia.org/wiki/Tour_Eiffel'
    ]

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    assert script.ApiWikipedia().get_information_place("tour eiffel") == results