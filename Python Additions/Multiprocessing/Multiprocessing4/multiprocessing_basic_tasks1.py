import multiprocessing
from time import perf_counter


def calculate_summ(begin, end, res_queue: multiprocessing.Queue):
    print(f'Process {multiprocessing.current_process().pid} started')
    total = sum(range(begin, end + 1))
    return res_queue.put(total)


if __name__ == '__main__':
    t1 = perf_counter()

    result_queue = multiprocessing.Queue()
    ranges = [(1, 250), (251, 500), (501, 750), (751, 1000)]

    processes = []
    for begin, end in ranges:
        p = multiprocessing.Process(target=calculate_summ, args=(begin, end))

    t2 = perf_counter()
    print(f'Working time: {t2 - t1:.2f} sec')
