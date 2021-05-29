import json

class Parser:

    def lower_string(self, string):
        return string.lower()

    def only_letters_in_string(self, string):
        new_string = ""
        for char in string:
            if char.isalpha():
                new_string += char
            else:
                new_string += " "
        return new_string.strip()

    def only_key_words_in_string(self, string):
        new_string = ""
        with open('GrandPyBot/stopwords-json/dist/fr.json') as json_list:
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
        