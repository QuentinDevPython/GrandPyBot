import parser as script

class TestParser:
    INPUT_STRING = "Pourrais-tu me dire où se trouve la Tour Eiffel ?"
    parser = script.Parser()
    
    def test_lower_string(self):
        new_string = self.parser.lower_string(self.INPUT_STRING)
        assert new_string == "pourrais-tu me dire où se trouve la tour eiffel ?"

    def test_only_letters_in_string(self):
        string = self.parser.lower_string(self.INPUT_STRING)
        new_string = self.parser.only_letters_in_string(string)
        assert new_string == "pourrais tu me dire où se trouve la tour eiffel"

    def test_only_key_words_in_string(self):
        string = self.parser.lower_string(self.INPUT_STRING)
        string = self.parser.only_letters_in_string(string)
        new_string = self.parser.only_key_words_in_string(string)
        assert new_string == "tour eiffel"