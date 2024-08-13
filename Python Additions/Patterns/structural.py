import time


def func_time_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = function(*args, **kwargs)
        end = time.time()
        print('Function took {} seconds'.format(end - start))
        return return_value

    return wrapper
