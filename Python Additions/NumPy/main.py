import numpy as np

from time import perf_counter


def working_time_prec(prec: int = 2):
    """Function for calculating working time of the methood in seconds"""

    def working_time(func):
        def wrapper(*args, **kargs):
            t1 = perf_counter()
            res = func(*args, **kargs)
            t2 = perf_counter()
            print(f'Working time: {t2 - t1:.{prec}f} sec, func: {func.__name__}')
            return res

        return wrapper

    return working_time


@working_time_prec(6)
def basics() -> None:
    """Basic"""

    n1 = np.array([1, 2, 3])  # Массив из списка
    n2 = np.zeros(3)  # Массив нулей
    n3 = np.ones(3)  # Массив единиц
    n4 = np.empty([3, 2], dtype=int)  # Массив произвольных данных
    n5 = np.arange(3)  # Массив из диапазона чисел
    n6 = np.arange(0, 12, 3)  # Массив из диапазона чисел
    n7 = np.linspace(0, 21, 8)  # Массив интервалов

    print(f'n1 shape: {n1}', f'n2 shape: {n2}', f'n3 shape: {n3}', f'n4 shape: {n4}', f'n5 shape: {n5}',
          f'n6 shape: {n6}', f'n7 shape: {n7}', sep='\n')
    print(f'type(n1) shape: {type(n1)}', f'dtype(n6): {n6.dtype}', f'size: {n6.size}', f'nbytes: {n6.nbytes}',
          f'ndim: {n6.ndim}', f'shape: {n6.shape}', sep='\n')

    n8 = np.arange(32).reshape(4, 8)
    print(n8, n8.ndim, n8.shape, sep='\n')


@working_time_prec()
def main() -> None:
    """Function only for run other program funcs"""

    basics()


if __name__ == '__main__':
    main()
