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

# Here i only notice that we have this algorithms
def linear_regression ():
    pass

@working_time_prec()
def main():



if __name__ == '__main__':
    main()
