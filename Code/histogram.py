import sys
import os
import re

def create_dict_histogram(words):
    """returns a histgram of text entered"""
    histo = {}
    for word in words:
        if word not in histo:
            histo[word] = 1
        else:
            histo[word] += 1
    return histo

def create_list_of_t_histogram(words):
    """create list of tuples histogram"""
    histo = list()
    for word in words:
        num = 0
        for entry in words:
            if word == entry:
                num += 1
        if (word, num) not in histo:
            histo.append((word, num))
    return histo

def create_l_of_l_histogram(words):
    """create list of lists histogram"""
    histo = list()

    for word in words:
        num = 0
        temp = list()
        for entry in words:
            if word == entry:
                num += 1
        temp.append(word)
        temp.append(num)
        if temp not in histo:
            histo.append(temp)
    return histo

def create_list_of_counts_histogram(words):
    counts_list = list()
    temp_dict = {}

    for i in range(len(words)):
        num = 0
        for entry in words:
            if entry == words[i]:
                num += 1
        # for key, value in temp_dict.items():
        if words[i] not in temp_dict.get(num, list()):
            temp_dict.setdefault(num, list()).append(words[i])
    for key, value in temp_dict.items():
        counts_list.append((key, value))
    return counts_list

def unique_words(histo):
    """returns number of unique words"""
    total_words = len(histo)
    return total_words

def unique_words_list(histo):
    count = list()
    for word in histo:
        if word not in count:
            count.append(word)
    return len(count)

def frequency_in_dict(histo, word):
    """returns frequency of a certain word in text"""
    if(word in histo):
        return histo[word]
    return False

def frequency_in_list(histo, word):
    """returns frequency of a certain word in text"""
    for i in range(len(histo)):
        # print(histo[i])
        if(histo[i][0] == word):
            return histo[i][1]
    return False

if __name__ == '__main__':

    with open("short_text.txt",'r') as file:
        text = file.read()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = text.split()

    for word in text:
        text.remove(word)
        text.append(word.lower())

    # histogram dict
    # dict = create_dict_histogram(text)
    # print(unique_words(dict))
    # print(frequency_in_dict(dict, sys.argv[1]))

    # histogram tuples
    # l_of_t = create_list_of_t_histogram(text)
    # print(unique_words_list(l_of_t))
    # print(frequency_in_list(l_of_t, sys.argv[1]))

    # histogram lists of lists
    # l_of_l = create_l_of_l_histogram(text)
    # print(unique_words_list(l_of_l))
    # print(frequency_in_list(l_of_l, sys.argv[1]))


    # # list of counts histogram
    counts_list = create_list_of_counts_histogram(text)
    print(counts_list)
