from collections import Counter
from random import randint
import time
from operator import itemgetter

candles = []

start_time = time.time()

for _ in range(10000000):
	candles.append(randint(0, 100))


def birthdayCakeCandles(ar):
    return max(Counter(ar).most_common(), key=lambda item: item[0])[1]

def boi(ar):
    return ar.count(ar.sort(reverse=True)[0])

def jj(ar):
    return ar.count(max(ar))

def fish(ar):
    ar.sort()
    return ar.count(ar[-1])




start_time2 = time.time()
print(jj(candles))
print("--- %s seconds ---" % (time.time() - start_time2))


start_time = time.time()
print(birthdayCakeCandles(candles))
print("--- %s seconds ---" % (time.time() - start_time))