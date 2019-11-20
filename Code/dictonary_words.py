import sys
import random
import requests
import json
import time

def new_sentence(words, number_of_words):
    result = ""
    for i in range(number_of_words):
        random_word = random.choice(words)
        random_word = random_word[:len(random_word)-2]
        result += random_word + " "
    return result

def vocab_game(words):

    random_word = random.choice(words)
    random_word = random_word[:len(random_word)-1]

    url = "https://wordsapiv1.p.rapidapi.com/words/{}/definitions".format(random_word)

    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "fa46af02fcmshbc148e63f17774bp123234jsnd5ced8dd6968"
        }

    response = requests.request("GET", url, headers=headers)

    resp_dict = json.loads(response.content)

    try:
        resp_dict['definitions'][0]['definition']
        print("What is the definition of {}(answer in 5 sec.)".format(random_word))
        time.sleep(5)
        print(resp_dict['definitions'][0]['definition'])
    except:
        vocab_game(words)

if __name__ == '__main__':
    words = list(open("/usr/share/dict/words","r"))
    # print(new_sentence(words, int(sys.argv[1])))

    keep_playing = True
    while(keep_playing):
        vocab_game(words)
        user_imput = input("Keep playing?(q to quite):")
        if user_imput is "q":
            keep_playing = False
