import dictogram
import random

class MarkovChain(dict):
    def __init__(self, word_list):
        super().__init__()
        for i in range(len(word_list)-1):
            first_word = word_list[i]
            self[first_word] = {}
            for j in range(len(word_list)-1):
                try:
                    count = self[first_word][word_list[j+1]]
                except KeyError:
                    count = 0
                if word_list[i] == word_list[j]:
                    count += 1
                    self[first_word][word_list[j+1]] = count
            tokens = 0
            for num in self[word_list[i]]:
                tokens+=self[word_list[i]][num]
            for count in self[word_list[i]]:
                self[word_list[i]][count] = (self[word_list[i]][count]/tokens)

    def sample(self, prev_word):
        random_num = random.random()
        fence = 0
        for elm in self[prev_word]:
            fence += self[prev_word][elm]
            if fence > random_num:
                return elm

    def random_walk(self, length=10):
        sentence = ""
        keys = list(self.keys())
        word = random.choice(keys)
        sentence += word + " "
        for i in range(length):
            word = self.sample(word)
            sentence += word + " "
        return sentence


if __name__ == '__main__':
    word_list = ["one", "fish", "one", "two", "fish", "two", "red", "fish", "blue", "red", "blue", "fish", "blue", "fish"]
    markovChain = MarkovChain(word_list)
    print(markovChain)
    print(markovChain.random_walk())
