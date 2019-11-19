import random
import re
from dictogram import Dictogram

class MarkovChain(Dictogram):
    def __init__(self, word_list):
        super().__init__()
        for i in range(len(word_list)-1):
            if word_list[i] in self:
                self[word_list[i].lower()].add_count(word_list[i+1].lower(), 1)
            else:
                self[word_list[i].lower()] = Dictogram([word_list[i+1].lower()])

    def random_walk(self, length=10):
        sentence = ""
        keys = list(self.keys())
        word = random.choice(keys)
        sentence += word + " "
        for i in range(length):
            word = self[word].sample()
            sentence += word + " "
        return sentence

if __name__ == '__main__':
    word_list = ["one", "blue", "fish", "one", "two", "fish", "two", "red", "fish", "blue", "red", "blue", "fish", "red", "blue", "fish"]
    markovChain = MarkovChain(word_list)
    print(markovChain)
    print(markovChain.random_walk(20))
