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


def symmetric_encryption():
    pass


def asymmetric_encryption():
    pass


@working_time_prec()
def main():
    symmetric_encryption()
    asymmetric_encryption()


if __name__ == '__main__':
    main()
