import sys

def begins_with(text, beginning):
    autocomplete_list = list()
    for word in text:
        if word.startswith(beginning):
            autocomplete_list.append(word)
    return autocomplete_list


if __name__ == '__main__':
    with open("/usr/share/dict/words",'r') as file:
        text = file.read().split()

    print(begins_with(text, sys.argv[1]))
