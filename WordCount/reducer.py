#!/usr/bin/python3

import sys

word_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
        word_count += count
    except:
        pass

print (word_count)