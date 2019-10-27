import sys

def create_dict_histogram(words):
    """returns a histgram of text entered"""
    histo = {}
    for word in words:
        if word not in histo:
            histo[word] = 1
        else:
            histo[word] += 1
    return histo

def create_list_histogram(words):
    """create list of lists histogram"""
    histo = list()
    for word in words:
        num = 0
        word = word.lower()
        for entry in words:
            entry = entry.lower()
            if word == entry:
                num += 1
        if (word, num) not in histo:
            histo.append((word, num))
    return histo

def create_l_of_t_histogram(words):
    """create list of tuples histogram"""
    histo = list()
    for i in range(len(words)):
        if (words[i], 1) in histo:
            print("HEREHEREHERE")
            for j in range(len(histo)):
                if(histo[j][0] == words[i]):
                    word = histo[j][0]
                    num = histo[j][1]
                    histo.remove(histo[j])
                    histo.append((word, num+1))
        else:
            histo.append((words[i], 1))
    return histo


def unique_words(histo):
    """returns number of unique words"""
    total_words = len(histo)
    return total_words

def unique_words_list(histo):
    count = {}
    for word in histo:
        if word not in count:
            count[word] = 1
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
        text = file.read().split()
    file.close()

    # dict = create_dict_histogram(text)
    l_of_l = create_list_histogram(text)
    # l_of_t = create_l_of_t_histogram(text)

    print(l_of_l)
    print(unique_words_list(l_of_l))
    print(frequency_in_list(l_of_l, sys.argv[1]))
