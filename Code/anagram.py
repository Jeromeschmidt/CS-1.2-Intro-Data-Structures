import sys
import random

def is_anagram(word_one, word_two):
    if word_one != word_two:
        return False
    return True

def create_dict_hash(words):
    dict = {}
    for i in range(len(words)):
        temp = sorted(words[i])
        temp = "".join(temp)
        dict[str(temp)] = str(words[i])
    return dict

def find_anagrams(dict_of_words, word):
    result = list()
    word1 = sorted(list(word))
    word1 = "".join(word1)
    for key in dict_of_words.keys():
        if(key in word1):
            result.append(dict_of_words.get(key))
    return result

if __name__ == '__main__':
    words = open("/usr/share/dict/words","r").read().split("\n")
    word = "listen"
    word1 = "silent"
    dict_of_words = create_dict_hash(words)
    # print(dict_of_words)
    list_of_anagrams = find_anagrams(dict_of_words, word1)
    print(list_of_anagrams)
