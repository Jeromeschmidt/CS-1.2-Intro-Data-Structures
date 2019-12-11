import random
import re
from dictogram import Dictogram
import string

class MarkovChain(Dictogram):
    def __init__(self, word_list, order):
        # super().__init__()
        self.order = order
        self.start_tokens = Dictogram()
        self.stop_tokens = Dictogram()

        ##### for first order MarkovChain
        word_list[0] = re.sub("[^a-zA-Z]", '', word_list[0])
        self.start_tokens.add_count(word_list[0].lower(), 1)

        for i in range(1, len(word_list)-1, 1):
            if((word_list[i][0].isupper()) and word_list[i-1][len(word_list[i-1])-1] in string.punctuation):
                # word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                if self.order > 1:
                    temp = list()
                    for j in range(self.order):
                        word_list[i+j] = re.sub("[^a-zA-Z]", '', word_list[i+j])
                        temp.append(word_list[i+j].lower())
                    if len(temp) > 1:
                        temp = tuple(temp)
                else:
                    word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                    temp = word_list[i].lower()
                self.start_tokens.add_count(temp, 1)
        for i in range(len(word_list)):
            if(word_list[i][len(word_list[i])-1] in string.punctuation):
                word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                # word_list[i] = word_list[i][:len(word_list[i])-1]
                self.stop_tokens.add_count(word_list[i], 1)
        for i in range(len(word_list)-self.order):
            if self.order > 1:
                temp = list()
                for j in range(self.order):
                    word_list[i+j] = re.sub("[^a-zA-Z]", '', word_list[i+j])
                    temp.append(word_list[i+j].lower())
                if len(temp) > 1:
                    temp = tuple(temp)
            else:
                word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                temp = word_list[i].lower()
            if temp in self:
                self[temp].add_count(word_list[i+self.order].lower(), 1)
            else:
                self[temp] = Dictogram([word_list[i+self.order].lower()])

            print(self.start_tokens)
    def random_walk(self, length=10):
        sentence = ""
        sentence = self.start_word().capitalize() + " "
        for i in range(length-self.order-1):
            next_word = self.sample(sentence)
            sentence += next_word + " "
        sentence += self.end_word() + "."
        return sentence

    def start_word(self):
        tokens = 0
        for elm in self.start_tokens:
            tokens += self.start_tokens[elm]
        dart = random.randrange(0, tokens)
        fence = 0
        for elm in self.start_tokens:
            fence += self.start_tokens[elm]
            if fence > dart:
                return elm

    def end_word(self):
        tokens = 0
        for elm in self.stop_tokens:
            tokens += self.stop_tokens[elm]
        dart = random.randrange(0, tokens)
        fence = 0
        for elm in self.stop_tokens:
            fence += self.stop_tokens[elm]
            if fence > dart:
                return elm

    def sample(self, sentence):
        word_list = sentence.split()
        word_list.reverse()
        for i in range(self.order):
            if len(word_list) < self.order:
                temp = list()
                temp = random.choice(self.keys())
                temp = tuple(temp)
            elif self.order > 1:
                temp = list()
                for j in range(self.order):
                    word_list[i+j] = re.sub("[^a-zA-Z]", '', word_list[i+j])
                    temp.append(word_list[i+j].lower())
                if len(temp) > 1:
                    temp = tuple(temp)
            else:
                word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                temp = word_list[i].lower()

        tokens = 0
        for value in self[temp].values():
            tokens += value
        dart = random.randrange(0, tokens)
        fence = 0
        for value in self[temp].values():
            fence += value
            if fence > dart:
                return list(self[temp])[0]

if __name__ == '__main__':
    words = "Blue fish blue fish. Blue fish blue fish."
    word_list = words.split()
    print(word_list)
    # word_list = ["Blue", "One.", "fish.", "One", "two","blue", "fish", "two", "red", "fish", "blue", "red", "blue", "fish", "red", "blue", "fish"]
    markovChain = MarkovChain(word_list, 2)
    print(markovChain)
    print(markovChain.random_walk(10))
