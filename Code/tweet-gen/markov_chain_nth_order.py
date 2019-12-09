import random
import re
from dictogram import Dictogram
import string

class MarkovChain(Dictogram):
    def __init__(self, word_list, order):
        super().__init__()
        self.order = order
        self.start_tokens = Dictogram()
        self.stop_tokens = Dictogram()

        ##### for first order MarkovChain
        word_list[0] = re.sub("[^a-zA-Z]", '', word_list[0])
        self.start_tokens.add_count(word_list[0].lower(), 1)

        for i in range(1, len(word_list)-1, 1):
            if((word_list[i][0].isupper()) and word_list[i-1][len(word_list[i-1])-1] in string.punctuation):
                word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                self.start_tokens.add_count(word_list[i].lower(), 1)
        for i in range(len(word_list)):
            if(word_list[i][len(word_list[i])-1] in string.punctuation):
                word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                # word_list[i] = word_list[i][:len(word_list[i])-1]
                self.stop_tokens.add_count(word_list[i], 1)
        for i in range(len(word_list)-self.order):
            temp = list()
            for j in range(self.order):
                word_list[i+j] = re.sub("[^a-zA-Z]", '', word_list[i+j])
                temp.append(word_list[i+j].lower())
            temp = tuple(temp)
            if temp in self:
                self[temp].add_count(word_list[i+self.order].lower(), 1)
            else:
                self[temp] = Dictogram([word_list[i+self.order].lower()])

    def random_walk(self, length=10):
        sentence = ""
        keys = list(self.keys())
        word = self.start_words()
        sentence += word + " "
        word = word.lower()
        for i in range(length-1):
            word = self[word].sample()
            sentence += word + " "
        sentence = sentence + self.end_word() + "."
        return sentence

    def start_words(self):
        keys = list(self.keys())
        words = random.choice(keys)
        if words[0] in self.stop_tokens:
            start_sentence = ""
            for i in range(len(words)):
                start_sentence += words[i] + " "
            return start_sentence
        else:
            self.start_words()

    def end_word(self):
        pass

if __name__ == '__main__':
    words = "Blue fish blue fish. Blue fish blue fish."
    word_list = words.split()
    print(word_list)
    # word_list = ["Blue", "One.", "fish.", "One", "two","blue", "fish", "two", "red", "fish", "blue", "red", "blue", "fish", "red", "blue", "fish"]
    markovChain = MarkovChain(word_list, 3)
    print(markovChain)
    print(markovChain.random_walk(20))
