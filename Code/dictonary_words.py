import sys
import random

def new_sentence(words, number_of_words):
    result = ""
    for i in range(number_of_words):
        random_word = random.choice(words)
        random_word = random_word[:len(random_word)-2]
        result += random_word + " "
    return result

if __name__ == '__main__':
    words = list(open("/usr/share/dict/words","r"))
    print(new_sentence(words, int(sys.argv[1])))
