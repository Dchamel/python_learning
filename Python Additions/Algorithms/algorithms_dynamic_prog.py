# Задача о Рюкзаке
# Рюкзак с ограниченым весом
# capacity = 10
# И набор предметов с разными весами
# weights = [2,3,5,7]
# и разной стоимостью
# values = [10,5,15,7]
# Положить наиболее ценные предметы, не превысив максимальный вес рюкзака(строго меньше)
import time
from time import perf_counter


def working_time_prec(prec=2):
    def working_time(func):
        def wrapper():
            t1 = perf_counter()
            func()
            t2 = perf_counter()
            print(f'Working time: {t2 - t1:.{prec}f} seconds')
            return func

        return wrapper

    return working_time


def bag(qwe):
    time.sleep(0.234234243)
    return qwe


@working_time_prec(9)
def main():
    qwe = 1
    bag(qwe)


if __name__ == '__main__':
    main()
