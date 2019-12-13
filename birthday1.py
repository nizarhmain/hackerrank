from collections import Counter
from random import randint
import time

import timeit


candles = []

for _ in range(100000):
    candles.append(randint(0, 100))


def birthdayCakeCandles(ar):
    return Counter(ar).most_common(1)[0][1]



start_time = time.time()
 
birthdayCakeCandles(candles)

elapsed_time = timeit.timeit(birthdayCakeCandles, number=100)/100
print(elapsed_time)