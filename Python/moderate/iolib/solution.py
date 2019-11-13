#!/usr/bin/env python

import time
import filecmp

INPUT_PATH = "myins.sql"


def timed(function):
    '''timing decorator'''
    def wrapper(*args, **kwargs):           # we don't know about arguments...
        start = time.time()
        result = function(*args, **kwargs)  # ...so we just pass what we got
        runtime = time.time() - start
        print('%s took %s seconds' % (function.__name__, runtime))
        return result
    return wrapper


@timed
def solution_one():
    '''
    Load complete file into memory, then perform replacements and write back
    to file. Needs a lot of memory, but is fast because we only do replacements
    once
    '''
    with open(INPUT_PATH, "r") as fin:
        data = fin.read()

    data = data.replace("`","")
    data = data.replace("0)","FALSE)")
    data = data.replace("1)","TRUE)")
    data = data.replace("'????'","NULL")

    with open("myinsR_ONE.sql", "w") as fout:
        fout.write(data)

@timed
def solution_two():
    '''
    Only read one line at time, do replacements and write line to output file.
    Needs nearly no memory, but takes longer than solution_one because of more
    replacement operations called
    '''
    with open(INPUT_PATH, "r") as fin:

        with open("myinsR_TWO.sql", "w") as fout:

            data = fin.readline()
            while data:
                data = data.replace("`","")
                data = data.replace("0)","FALSE)")
                data = data.replace("1)","TRUE)")
                data = data.replace("'????'","NULL")
                fout.write(data)
                data = fin.readline()


# seperate operations using sleep to create more readable plot hwen using
# memory_profiler
solution_one()
time.sleep(2)
solution_two()
time.sleep(2)
assert filecmp.cmp("myinsR_ONE.sql", "myinsR_TWO.sql"), 'Result files differ!'
