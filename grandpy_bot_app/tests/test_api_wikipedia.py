"""Import the module urllib.request to open URLs (HTTP)
in a complex world.
Import also the file which is going to be tested (api_wkipedia)."""
import urllib.request

from .. import api_wikipedia as script


def test_http_result(monkeypatch):
    """
    Method which compares the expected results of the API function
    with the results obtained by this simulation
    """
    
    results = [
        'Cathédrale Notre-Dame de Paris',
        'La cathédrale Notre-Dame de Paris, '
        'communément appelée Notre-Dame, '
        'est l\'un des monuments les plus '
        'emblématiques de Paris et de la France. '
        'Elle est située sur l\'île de la Cité et '
        'est un lieu de culte catholique, siège de '
        'l\'archidiocèse de Paris, dédié à la Vierge '
        'Marie.\nCommencée sous l\'impulsion de '
        'l\'évêque Maurice de Sully, sa construction '
        's\'étend sur environ deux siècles, de 1163 '
        'au milieu du XIVe siècle.',
        'https://fr.wikipedia.org/wiki/Cath%C3%A9drale_Notre-Dame_de_Paris'
    ]

    def mockreturn():
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    assert script.ApiWikipedia().get_information_place("notre dame paris") == results
