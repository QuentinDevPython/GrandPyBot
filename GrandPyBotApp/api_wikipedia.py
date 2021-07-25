import wikipedia

class ApiWikipedia:

    def __init__(self, place):
        self.wikipedia = wikipedia
        self.wikipedia.set_lang('fr')
        self.place = place
        self.place_page = self.wikipedia.page(place)

    def get_information_place(self):
        wiki_result = [self.place_page.title, self.wikipedia.summary(self.place, sentences=3), self.place_page.url]
        if len(wiki_result) > 0:
            return wiki_result