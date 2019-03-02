#!/usr/bin/env python

import time
import sys

if sys.version_info[0] == 2:
    range = xrange

EXP = 3  # 10 ** 3 = 1000 is highest limit!
LIMITS = [10 ** i for i in range(2, EXP + 1)]


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
def solution_one(limit):
    value = 0

    for i in range(1, limit):
        if (i % 3 == 0) or (i % 5 == 0):
            value += i

    return value


@timed
def solution_two(limit):
    '''
    using sum builtin and a generator expression.
    note that there is no need to wrap the input of sum() into a list,
    as the generator expression creates an iterator itself. this is not
    allowed in zope python code.

    not faster than solution_one.
    '''
    return sum(
        number for number in range(1, limit)
        if (number % 3 == 0) or (number % 5 == 0)
    )


def main():
    '''program starts here. we call all solution variants and compare results,
    assuming they are same'''

    for limit in LIMITS:
        print('Limit: %s' % limit)
        time.sleep(1)
        res_one = solution_one(limit)
        res_two = solution_two(limit)

        # check results
        print('Result is %s' % res_one)
        assert res_one == res_two, 'results must be same!'


if __name__ == "__main__":
    main()
