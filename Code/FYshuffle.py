import random
import sys

# numbers = list()
# for i in range(10):
#     numbers.append(i)
#
# new_list = list()
#
# for i in range(len(numbers)):
#     random_elm = random.choice(numbers)
#     new_list.append(random_elm)
#     numbers.remove(random_elm)
# print(numbers)
# print(new_list)

def FYS(elms):
    new_list = list()
    for i in range(len(elms)):
        random_elm = random.choice(elms)
        new_list.append(random_elm)
        elms.remove(random_elm)
    return new_list

if __name__ == '__main__':
    numbers = list()
    for i in range(int(sys.argv[1])):
        numbers.append(i)

    print("original list: " + str(numbers))

    shuffled_list = FYS(numbers)
    print("FY shuffled list: " + str(shuffled_list))
