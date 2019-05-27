import os
import math
import time
from multiprocessing import Process,Queue,Manager

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

def turboRange(bekannte_prims,start,limit,num):
    '''super turbo version'''
    result = []
    for number in range(start, limit):
        isprime = True
        for divisor in bekannte_prims:  # we only have to check for prime numbers!
            if divisor ** 2 > number:  # we can also stop checking here!
                break                  # such divisors cannot occur in factorization
            if number % divisor == 0:
                isprime = False
                break  # we can stop checking here!
        if isprime:
            bekannte_prims.append(number)
            result.append(number)
    return_vals[num] = result
    return result



@timed
def turboPrallel(limit):
    needed_prims = int(math.ceil(math.sqrt(limit)))
    bekannte_prims = turboNoTime(needed_prims)
    start = len(bekannte_prims)


    process_count = 10
    missing_prim_count = start
    prims_per_process = int(math.floor((limit - missing_prim_count) / process_count))



    processes=[]
    for i in range(0,process_count):
        if i == process_count-1:
            processes.append(Process(target=turboRange,args = (bekannte_prims, start,int(limit),i)))
            break
        processes.append(Process(target=turboRange,args = (bekannte_prims, start,start+prims_per_process,i)))
        start+=prims_per_process



    for i in range(0,process_count):
        processes[i].start()

    for i in range(0,process_count):
        processes[i].join()
        bekannte_prims.extend(return_vals[i])
    return bekannte_prims


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


limit = input("Obere Schranke fuer Primzahlenberechnung eingeben")
turboPrallel(limit)
turbo(limit)
sumMethod(limit)
