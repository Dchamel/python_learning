import multiprocessing

lock = multiprocessing.Lock()


def get_value(l):
    l.asquire()


multiprocessing.Process(target=get_value, args=(lock,)).start()
