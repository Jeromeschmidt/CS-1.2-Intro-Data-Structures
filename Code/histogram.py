from string import punctuation
import re

def create_histogram(words):
    """returns a histgram of text entered"""
    hista = {}
    for word in words:
        if word not in hista:
            hista[word] = 1
        else:
            hista[word] += 1
    return hista

def unique_words(hista):
    """returns number of funique words"""
    total_words = len(hista)
    return total_words

def frequency(hista, word):
    """returns frequency of a certain word in text"""
    if(word in hista):
        return hista[word]
    return False

if __name__ == '__main__':
    words = ""
    punctuation = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~¢½Â£¨')
    text = list(open("sherlock.txt",'r').read().strip())
    dict = create_histogram(text)
    for punc in punctuation:
        print(punc)
        if(punc in dict):
            while(punc in dict):
                dict.pop(punc)

    # for line in text.readlines():
    #     temp = line.readline()
    # for line in text:
    #     for word in line:
    #         words = ''.join([word for word in text if letter not in punctuation])
    #print("".join(text))
    print(dict)#create_histogram("".join(text)))
    print(unique_words(create_histogram(text)))
    print(frequency(create_histogram(text), "mystery"))
    # print(text)
