import wikipedia

class ApiWikipedia:

    def __init__(self):
        self.wikipedia = wikipedia
        self.wikipedia.set_lang('fr')

    def get_information_place(self, place):
        place_page = self.wikipedia.page(place)
        wiki_result = [place_page.title, self.wikipedia.summary(place, sentences=3), place_page.url]
        if len(wiki_result) > 0:
            return wiki_result