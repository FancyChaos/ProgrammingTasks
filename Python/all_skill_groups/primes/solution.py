#!/usr/bin/env python
'''
Some example solutions, using a decorator to measure function runtime.
Demonstrates how simple code/algorithm changes can have a major performance impact.

Intended to run in python3
'''

import time

LIMIT = 100000


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
def simple():
    '''simple solution'''
    result = []
    for number in range(2, LIMIT):
        isprime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                isprime = False
        if isprime:
            result.append(number)

    return result


@timed
def faster():
    '''faster variant of simple'''
    result = []
    for number in range(2, LIMIT):
        isprime = True
        for divisor in result:  # we only have to check for prime numbers!
            if number % divisor == 0:
                isprime = False
        if isprime:
            result.append(number)

    return result


@timed
def even_faster():
    '''even faster variant of faster'''
    result = []
    for number in range(2, LIMIT):
        isprime = True
        for divisor in result:  # we only have to check for prime numbers!
            if number % divisor == 0:
                isprime = False
                break  # we can stop checking here!
        if isprime:
            result.append(number)

    return result


@timed
def turbo():
    '''super turbo version'''
    result = []
    for number in range(2, LIMIT):
        isprime = True
        for divisor in result:  # we only have to check for prime numbers!
            if divisor ** 2 > number:  # we can also stop checking here!
                break                  # such divisors cannot occur in factorization
            if number % divisor == 0:
                isprime = False
                break  # we can stop checking here!
        if isprime:
            result.append(number)

    return result


def main():
    '''program starts here. we call all function variants and compare results,
    assuming they are same'''

    simple_res = simple()
    faster_res = faster()
    even_faster_res = even_faster()
    turbo_res = turbo()

    # check results
    assert simple_res == faster_res, 'results must be same!'
    assert simple_res == even_faster_res, 'results must be same!'
    assert simple_res == turbo_res, 'results must be same!'

    print('Limit was %s' % LIMIT)


if __name__ == "__main__":
    main()
