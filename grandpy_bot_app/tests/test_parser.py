"""Import the file which is going to be tested (parser)."""
from .. import parser as script


class TestParser:
    """
    Class that tests the parser.

    Args:
        INPUT_STRING (the sentence that we want to test)
        parser (object of the tested class Parser)
    """
    INPUT_STRING = "Pourrais-tu me dire où se trouve la Tour Eiffel ?"
    parser = script.Parser()

    def test_lower_string(self):
        """
        Method that tests the lower_string function.
        The function lower_string puts the sentence in lowercase.
        """
        new_string = self.parser.lower_string(self.INPUT_STRING)
        assert new_string == "pourrais-tu me dire où se trouve la tour eiffel ?"

    def test_only_letters_in_string(self):
        """
        Method that tests the only_letters_in_string function.
        The only_letters_in_string function deletes the characters in the
        sentence that are not letters.
        """
        string = self.parser.lower_string(self.INPUT_STRING)
        new_string = self.parser.only_letters_in_string(string)
        assert new_string == "pourrais tu me dire où se trouve la tour eiffel"

    def test_only_key_words_in_string(self):
        """
        Method that tests the only_key_words_in_string function.
        The only_key_words_in_string function deletes the words in the
        sentence that are not key words.
        """
        string = self.parser.lower_string(self.INPUT_STRING)
        string = self.parser.only_letters_in_string(string)
        new_string = self.parser.only_key_words_in_string(string)
        assert new_string == "tour eiffel"

    def test_parser(self):
        """
        Method that tests the parser function.
        The parser function combines all the methods of the class Parser
        to obtain the final sentence.
        """
        string = self.parser.parser(self.INPUT_STRING)
        assert string == "tour eiffel"
