"""Import the module googlemaps to access to the Wikipedia information."""
import wikipedia


class ApiWikipedia:
    """
    Class that allows to get the wikipedia information.

    Args:
        wikipedia (object to access Wikipedia, the language is set to french)
    """

    def __init__(self):
        self.wikipedia = wikipedia
        self.wikipedia.set_lang('fr')

    def get_information_place(self, place):
        """
        Function that returns the wikipedia information about the place in parameter
        and the title of the page found.
        """
        place_page = self.wikipedia.page(place)
        wiki_result = [place_page.title, self.wikipedia.summary(
            place, sentences=3), place_page.url]
        if len(wiki_result) > 0:
            return wiki_result
        return None
