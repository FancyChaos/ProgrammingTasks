import os
import math
import time
import sys
from multiprocessing import Process,Queue,Manager,cpu_count

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
def turbo(LIMIT):
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

def turboNoTime(LIMIT):
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

def turboRange(known_prims,start,limit,num):
    '''super turbo version'''
    result = []
    for number in range(start, limit):
        isprime = True
        for divisor in known_prims:  # we only have to check for prime numbers!
            if divisor ** 2 > number:  # we can also stop checking here!
                break                  # such divisors cannot occur in factorization
            if number % divisor == 0:
                isprime = False
                break  # we can stop checking here!
        if isprime:
            result.append(number)
    return_vals[num] = result



@timed
def turboPrallel(limit):
    '''
    Uses multiprocessing to accelerate prime number calculation using the turbo
    function from primes excercise solution. Steps:

    - precalculate needed prime numbers to build chunks for parallel calculation
    - set up chunks and pass them to processes created via multiprocessing
      module
    - start processes, wait for them to finish and fetch results
    '''

    # precalculation
    needed_prims = int(math.ceil(math.sqrt(limit)))
    known_prims = turboNoTime(needed_prims)
    start = known_prims[-1] + 1

    # process setup
    process_count = cpu_count()
    prims_per_process = int(math.floor((limit - start) / process_count))
    processes = []
    for proc_index in range(process_count):

        # make sure we calculate exactly to the limit
        if proc_index == process_count - 1:
            end = limit
        else:
            end = start + prims_per_process

        proc = Process(
            target=turboRange,
            args = (known_prims, start, end, proc_index)
        )
        processes.append(proc)
        proc.start()
        start+=prims_per_process

    # wait for procs and and fetch results
    for index, proc in enumerate(processes):
        proc.join()
        known_prims.extend(return_vals[index])

    return known_prims


@timed
def sumMethod(n):
    prim = [2,3]
    primSum = [0,0];
    check = 5
    while check <n:
        primIndex=0
        bound = math.sqrt(check)
        #print("Check:"+str(check))
        while prim[primIndex] <= bound:
            #print("Test:"+str(prim[primIndex]))
            if primSum[primIndex] == check:
                #print("=>teilbar durch"+str(prim[primIndex])+"\n")
                break
            elif primSum[primIndex] > check:
                #print("->nicht teilbar durch"+str(prim[primIndex]))
                primIndex+=1
                continue
            else:
                while primSum[primIndex]< check:
                    primSum[primIndex] += prim[primIndex]
                    #print("PrimSum:"+str(primSum[primIndex]))
                    if primSum[primIndex] == check:
                        break
                    if primSum[primIndex] > check:
                        #print("->nicht teilbar durch"+str(prim[primIndex]))
                        primIndex+=1
                        break
        else:
            prim.append(check);
            #print("=>Primzahl"+"\n")
            primSum.append(check)
        check+=1
    return prim


manager = Manager()
return_vals = manager.dict()

# use argument script is called with or ask user for limit
if len(sys.argv) == 2:  # this is very lazy, use argparse for complicated stuff
    limit = int(sys.argv[1])
else:
    limit = input("Please enter upper limit for prime number calculation: ")

# fetch results, sort (for comparison), cast to list (python3)
res1 = list(sorted(turboPrallel(limit)))
res2 = list(sorted(turbo(limit)))
res3 = list(sorted(sumMethod(limit)))

assert res1 == res2, 'Results 1 and 2 do not match! %s != %s' % (res1, res2)
assert res1 == res3, 'Results 1 and 3 do not match! %s != %s' % (res1, res3)
