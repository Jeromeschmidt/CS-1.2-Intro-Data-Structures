import random
import re
from dictogram import Dictogram

class MarkovChain(Dictogram):
    def __init__(self, word_list):
        super().__init__()
        self.start_tokens = Dictogram()
        self.stop_tokens = Dictogram()
        for i in range(len(word_list)-1):
            if word_list[i] in self:
                self[word_list[i].lower()].add_count(word_list[i+1].lower(), 1)
                if word_list[i][0].isupper():
                    self.start_tokens.add_count(word_list[i], 1)
            else:
                self[word_list[i].lower()] = Dictogram([word_list[i+1].lower()])
                if word_list[i][0].isupper():
                    self.start_tokens.add_count(word_list[i], 1)

    def random_walk(self, length=10):
        sentence = ""
        keys = list(self.keys())
        # word = random.choice(keys)
        word = self.start_word()
        sentence += word + " "
        word = word.lower()
        for i in range(length-1):
            word = self[word].sample()
            sentence += word + " "
        word = self.end_word() + ". "
        return sentence

    def start_word(self):
        dart = random.randint(0, len(self.start_tokens))
        fence = 0
        for elm in self.start_tokens:
            for key in self.start_tokens.keys():
                fence += self.start_tokens[key]
                if fence > dart:
                    return elm.capitalize()

    def end_word(self):
        dart = random.randint(0, len(self.stop_tokens))
        fence = 0
        for elm in self.stop_tokens:
            for key in self.stop_tokens.keys():
                fence += self.stop_tokens[key]
                if fence > dart:
                    return elm

if __name__ == '__main__':
    word_list = ["One", "blue", "fish.", "One", "two", "fish", "two", "red", "fish", "blue", "red", "blue", "fish", "red", "blue", "fish"]
    markovChain = MarkovChain(word_list)
    print(markovChain)
    print(markovChain.random_walk(20))
