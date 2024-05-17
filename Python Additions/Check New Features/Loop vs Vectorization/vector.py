# About Vectorization instead of Loops
# https://www.geeksforgeeks.org/convert-string-to-long-in-python/

from time import perf_counter
import numpy as np
import hashlib, random

# average execution time is 0,14-0,17 sec
t1 = perf_counter()
all = 0
for each in range(0, 1500000):
    all += each
print(all)
t2 = perf_counter()
t3_loop = t2 - t1
print(f'Loop Traditional: {t3_loop:.5f} sec')

# average execution time for "Vanilla" method
# with conversion to Float
# is about 0,13-0,15 sec
t1 = perf_counter()
print(sum(np.arange(float(1500000))))
t2 = perf_counter()
t3_van = t2 - t1
print(f'Vanilla Sum Float: {t3_van:.5f} sec')

# average execution time for "Vectorization"(SIMD) method
# with conversion to Float
# is about 0,13-0,15 sec
t1 = perf_counter()
print(np.sum(np.arange(float(1500000))))
t2 = perf_counter()
t3_vector = t2 - t1
print(f'Vectorization Float: {t3_vector:.5f} sec')

print(f'Vect faster than LOOP in: {t3_loop / t3_vector:.2f} times')
print(f'Vect faster than Vanilla Sum in: {t3_van / t3_vector:.2f} times')
