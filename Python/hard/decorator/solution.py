#!/usr/bin/env python

import inspect
from collections import Counter
import random
import time


def lucky_res(func):
    '''
    lets memorize all results but return a random choice, don't tell anyone
    about it.
    first call will be fine but from then it's all about luck!
    adds extra fun due to fuzzy results and increased memory overhead
    '''
    results = []

    def inner(*args, **kwargs):
        results.append(func(*args, **kwargs))
        return random.choice(results)
    return inner


def throw_coin(func):
    '''
    Throw a coin wether to call function and return or throw useless error

    Sleeps built in to raise excitement during execution
    '''
    def inner(*args, **kwargs):
        print('Will throw coin to decide if %s is executed' % func.__name__)
        time.sleep(1)
        lucky = random.randint(0, 1)
        if lucky:
            print('Congratualtions! Your function will be executed!')
            time.sleep(1)
            return func(*args, **kwargs)
        else:
            raise Exception('Bad luck.')

    return inner


def call_counter(num_calls):
    '''
    limit calls of a function to num_calls for absolutely no reason
    throw error when call limit is exceeded
    '''
    calls = {}

    def inner(func):

        def func_wrapper(*args, **kwargs):
            if func not in calls:
                calls[func] = 0
            else:
                calls[func] += 1
            if calls[func] < num_calls:
                return func(*args, **kwargs)
            else:
                raise AssertionError(
                    'We are sorry. No more calls left for %s' % func.__name__
                )

        return func_wrapper

    return inner


def forbidden_chars(chars):
    '''
    only execute function if function source code does not contain forbidden
    charaters. because we do not like code having certain characters
    '''
    def inner(func):
        def func_wrapper(*args, **kwargs):
            # filter forbidden_chars decorator line from source
            func_source = '\n'.join(
                line for line in inspect.getsource(func).split('\n')
                if '@forbidden_chars' not in line
            )
            forbidden = any(char in func_source for char in chars)
            assert not forbidden, 'Your function contains forbidden characters: %s' % chars
            return func(*args, **kwargs)
        return func_wrapper
    return inner


def char_counter(char_map):
    '''
    only execute function if function source code does not contain forbidden
    charaters
    '''
    def inner(func):
        def func_wrapper(*args, **kwargs):
            # filter forbidden_chars decorator line from source
            func_source = '\n'.join(
                line for line in inspect.getsource(func).split('\n')
                if '@char_counter' not in line
            )
            source_counter = dict(Counter(func_source))
            for character, limit in char_map.items():
                if character in source_counter and source_counter[character] > limit:
                    raise AssertionError(
                        'Limit for character %s of %s exceeded!' % (character, limit)
                    )
            return func(*args, **kwargs)
        return func_wrapper
    return inner


@call_counter(5)
def say_hello():
    print('Hello World')


@char_counter({'x': 20})
@forbidden_chars('k')
def something_else(matters):
    print(matters)


@lucky_res
def complex_calc(number):
    return number * 2


@throw_coin
def important_function(something):
    print('VERY important calculations executing')
    return something + 1


if __name__ == "__main__":
    for _ in range(10):
        try:
            say_hello()
        except Exception as e:
            print(e)
    something_else('Wello Horld')

    doubles = [(d, complex_calc(d)) for d in range(10)]
    print(doubles)

    important_function(1)
