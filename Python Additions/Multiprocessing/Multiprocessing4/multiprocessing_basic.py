import multiprocessing


def worker(name):
    print(f'Worker {name} started')
    print(f'PID: {multiprocessing.current_process().pid}')


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=('Alice',))
    p.start()
    p.join()
    print('Main process finished.')
