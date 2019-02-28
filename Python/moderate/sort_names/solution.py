#!/usr/bin/env python

import os
import sys
import io
import string

# very simple argument handling to alter file examined
if len(sys.argv) == 2:
    list_path = sys.argv[1]
else:
    list_path = 'names.txt'

# avoid errors due to relative path of names.txt
if not os.path.isfile(list_path):
    print('Please call me inside the Python/moderate/sort_names folder!')
    sys.exit(1)

# read list of names from file
# use io.open = open() in python3
# provding explicit encoding and error handling is neccessary for evil_list
# challenge
with io.open(list_path, 'r', encoding='utf-8', errors='ignore') as f:
    name_list_raw = f.read()
    name_list = name_list_raw.replace('"', '').split(',')

# name_list cleanup needed for evil_list challenge
name_list = [
    name.strip() for name in name_list
    if name and name[0] in string.ascii_letters
]

# use lambda here instead of str.lower and unicode.lower to provide
# python2 and python3 compatibility
ordered_names = sorted(name_list, key=lambda x: x.lower())

print("Ordered names:")
print(ordered_names)
print('There are {} names in the list'.format(len(name_list)))
