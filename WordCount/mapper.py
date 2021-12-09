#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    words_list = line.split()

    for word in words_list:
        print(word + "\t" + str(1))
