import wikipedia
import json

class ApiWikipedia:

    def __init__(self):
        self.wikipedia = wikipedia.set_lang('fr')
        self.place_page = wikipedia.page("tour eiffel") #Import the page asked by the user

    def get_information_place(self):
        with open('wiki_place.json', 'w') as json_file:
            wiki_result = [self.place_page.title, self.wikipedia.summary('tour eiffel', sentences=3)]
            if len(wiki_result) > 0:
                json.dump(wiki_result,json_file)