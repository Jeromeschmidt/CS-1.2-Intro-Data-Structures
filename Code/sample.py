import sys
import random

def find_weights(text):
    weights = {}
    size = len(text)
    for word in text:
        count = 0
        for word2 in text:
            if(word == word2):
                count += 1
        weights[word] = (count/size)
    return weights


def run(weights, number_of_iter):
    keys_list = list(weights.keys())
    weights_list = list(weights.values())
    results = {}
    for i in range(number_of_iter):
        # random_word = random.choices(keys_list, weights_list)[0]
        for key in keys_list:
            if(random.random() < weights[key]):
                if key in results:
                    results[key] += 1
                else:
                    results[key] = 1
    return results

if __name__ == '__main__':
    file = sys.argv[1]
    text = open(file,"r").read().split()
    dict = find_weights(text)
    print(run(find_weights(text), 10000))
