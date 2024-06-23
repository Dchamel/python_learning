import multiprocessing
from time import perf_counter
from random import randint, randrange
import time

t1 = perf_counter()


def job(x):
    name_proc = multiprocessing.current_process().name
    print(name_proc)
    res = round(((((x ** 100 / 1234 + 1 / 4) / 2 ** 43 * 3.12 / 3.45) % 3) * 2) / 1.23, 3)
    # sleep_time = randint(1, 4)
    # time.sleep(sleep_time)
    # print(f'Job`s time: {sleep_time} sec')
    return res


jobs_no = 4
inp_data1 = range(1, 20)
inp_data2 = range(1, 5)
inp_data2 = map(lambda x: randint(1, 20) * x, inp_data2)
print(inp_data2)

with multiprocessing.Pool(1) as pool:
    print('Results:')
    job1 = pool.map(job, inp_data1)
    job2 = pool.map(job, inp_data2)

t2 = perf_counter()
print(f'Working time: {t2 - t1:.2f} sec')
