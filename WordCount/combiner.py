#!/usr/bin/python3

import sys

words_dict = dict()

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
        if word in words_dict:
            words_dict[word] += count
        else:
            words_dict[word] = 1
    except:
        pass

for element in words_dict.items():
    print(element[0] + "\t" + str(element[1]))