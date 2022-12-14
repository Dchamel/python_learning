# About Vectorization instead of Loops
# https://www.geeksforgeeks.org/convert-string-to-long-in-python/

from time import perf_counter
import numpy as np

# average execution time is 0,14-0,17 sec
t1 = perf_counter()
all = 0
for each in range(0, 1500000):
    all += each
print(all)
t2 = perf_counter()
print(f'Loop Traditional: {t2 - t1:.5f} sec')

# average execution time for "Vectorization" method
# with conversion to Float
# is about 0,13-0,15 sec
t1 = perf_counter()
print(sum(np.arange(float(1500000))))
t2 = perf_counter()
print(f'Vectorization Float: {t2 - t1:.5f} sec')

# average execution time for "Vectorization" method
# with conversion to Bigint
# is about 0,13-0,15 sec
t1 = perf_counter()
print(sum(np.arange(1500000)))
t2 = perf_counter()
print(f'Vectorization Float: {t2 - t1:.5f} sec')
