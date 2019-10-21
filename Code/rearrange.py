import sys
import random

def rearrange(test):
    result = ""
    for i in range(len(test)):
        random_word = random.choice(test)
        result += random_word + " "
        test.remove(random_word)
    return(result)


if __name__ == '__main__':
    test = list(sys.argv[1:])
    print(rearrange(test))
