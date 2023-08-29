# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word =word

    def match(self, words):
        lower_self_word = self.word.lower()
        return [word for word in words if sorted(word.lower()) == sorted(lower_self_word)and word.lower() != lower_self_word]

