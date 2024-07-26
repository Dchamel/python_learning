from time import perf_counter


def working_time_prec(prec=2):
    def working_time(func):
        def wrapper(*args, **kwargs):
            t1 = perf_counter()
            ret = func(*args, **kwargs)
            t2 = perf_counter()
            print(f'Working time: {t2 - t1:.{prec}f} seconds. Function: {func.__name__}')
            return ret

        return wrapper

    return working_time


def main() -> None:
    """
    Main function of the file.
    Only for run other functions or main functional
    """
    pass


if __name__ == '__main__':
    main()
