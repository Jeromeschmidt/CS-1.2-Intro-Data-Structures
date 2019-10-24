import sys

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

    with open("sherlock.txt",'r') as file:
        text = file.read().split()

    dict = create_histogram(text)

    print(unique_words(create_histogram(text)))
    print(frequency(create_histogram(text), sys.argv[1]))
