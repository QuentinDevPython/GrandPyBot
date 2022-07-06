"""Import the module json to create json files."""
import json


class Parser:
    """
    Class that parses a sentence.

    Args:
        None
    """

    def lower_string(self, string):
        """
        Function that puts the sentence in lowercase.
        """
        return string.lower()

    def only_letters_in_string(self, string):
        """
        Function that deletes the characters in the
        sentence that are not letters.
        """
        new_string = ""
        for char in string:
            if char.isalpha():
                new_string += char
            else:
                new_string += " "
        return new_string.strip()

    def only_key_words_in_string(self, string):
        """
        Function that deletes the words in the
        sentence that are not key words.
        """
        new_string = ""
        with open('grandpy_bot_app/stopwords-json/dist/fr.json') as json_list:
            key_word_list = json.load(json_list)
        for word in string.split(' '):
            status = False
            for key_word in key_word_list:
                if word == key_word:
                    status = True
                    break
            if not status:
                new_string += word + ' '
        return new_string.strip()

    def parser(self, string):
        """
        Function that combines all the methods of the class Parser
        to obtain the final sentence.
        """
        string = self.lower_string(string)
        string = self.only_letters_in_string(string)
        string = self.only_key_words_in_string(string)
        return string