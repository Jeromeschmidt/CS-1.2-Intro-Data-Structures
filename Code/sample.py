import sys
import random
from utils import time_it
# random.seed(42)

@time_it
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

@time_it
def find_weights_list(text):
    weights = list()
    size = len(text)
    for word in text:
        count = 0
        for word2 in text:
            if(word == word2):
                count += 1
        if((word, count/size) not in weights):
            weights.append((word, count/size))
    return weights

@time_it
def run_list(weights, number_of_iter):
    results = list()
    for elm in weights:
        results.append((elm[0], elm[1], 0))
    for i in range(number_of_iter):
        for elm2 in results:
            if(random.random() < elm2[1]):
                word = elm2[0]
                prob = elm2[1]
                num = elm2[2]
                results.remove(elm2)
                results.append((word, prob, num+1))
    # number_of_iter = int(number_of_iter/2)
    # results = list()
    # for word in weights:
    #     results.append((word[0], 0))
    # flag = True
    # total_count = 0
    # while flag:
    #     for elm in weights:
    #         count = 0
    #         if(random.random() < elm[1]):
    #             for elm2 in results:
    #                 if(elm2[0] == elm[0]):
    #                     total_count+=1
    #                     temp = elm2[1]
    #                     results.remove(elm2)
    #                     results.append((elm[0], temp+1))
    #                 if(total_count >= number_of_iter):
    #                     return results
    #     if(total_count >= number_of_iter):
    #         flag = False
    return results

@time_it
def run(weights, number_of_iter):
    keys_list = list(weights.keys())
    weights_list = list(weights.values())
    results = {}
    for i in range(number_of_iter):
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
    list_weights = find_weights_list(text)
    print(run(dict, 1000000))
    print(run_list(list_weights, 1000000))
