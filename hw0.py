'''
    You will only be writing code in this file and this is the only file submitted to the autograder.
'''
import sys
import csv


def get_version():
    version = sys.version
    version_number = version[0:5]
    print(version_number)


def alternative_sum(start, n):
    return_list = [start]  # plug starting value into list
    for a in range(n - 1):  # since we already have the first value, we iterate n-1 times
        if len(return_list) < 3:  # since we sum last-3rd and last items, there must be at least 3 items, else last*2
            return_list.append(return_list[-1] * 2)
        else:
            return_list.append(return_list[-1] + return_list[-3])
    return return_list


def order_scores():
    return_list = []  # contains list of names
    d = {}  # contains the dictionary of name:score
    with open('scores.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for p in reader:
            d[p[0]] = p[1]  # map all names to values
    del d["name"]  # remove the name, score values
    sorted_d = sorted(d.items(), key=lambda val: val[1])
    # print(sorted_d)
    for a in sorted_d:
        return_list.append(a[0])
    # print(return_list)
    return return_list

# testing #
# get_version()

# asd = alternative_sum(15,5)
# print(asd)

# order_scores()
