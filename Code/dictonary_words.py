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
    dict = create_dict_hash(words)
    print(new_sentence(words, int(sys.argv[1])))
    word1 = random.choice(words)
    # word1 = word1[:len(word1)-2]
    word2 = random.choice(words)
    # word2 = word2[:len(word2)-2]
    if(sorted(word1) in dict):
        print("1111")
    # while(is_anagram(word1, word2) == False):
    #     word1 = random.choice(words)
    #     word1 = word1[:len(word1)-2]
    #     word2 = random.choice(words)
    #     word2 = word2[:len(word2)-2]
