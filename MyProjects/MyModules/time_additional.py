# Extension module for working with time
# for IMPORT only

from time import perf_counter


def working_time_prec(prec: int = 2):
    """Func for calculating func working time"""

    def working_time(func):
        def wrapper():
            t1 = perf_counter()
            res = func()
            t2 = perf_counter()
            print(f'Working time: {t2 - t1:.{prec}f} sec, func: {func.__name__}')
            return res

        return wrapper

    return working_time


if __name__ == '__main__':
    print("Module for import only")
