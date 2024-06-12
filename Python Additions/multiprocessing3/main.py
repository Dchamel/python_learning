# n! = (1,2,3,4,5)
from time import perf_counter
from multiprocessing import Pool, current_process


def working_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        content = func(*args, **kwargs)
        t2 = perf_counter()
        print(f'Working time: {t2 - t1:.2f} seconds')
        return content

    return wrapper


def fac(n):
    return 1 if n <= 0 else n * fac(n - 1)


def main(n: int):
    res = fac(n)
    res = hash(res)
    print(current_process().name)
    return res


if __name__ == '__main__':
    @working_time
    def run():
        num = 990
        num_range = range(1, num + 1)
        with Pool(processes=61) as pool:
            res = pool.map(main, num_range)

        print(res)


    run()
