# LOCK
# import multiprocessing
# import time
# from multiprocessing import Process, Lock
# from time import perf_counter
#
#
# def get_value(locked: Lock):
#     locked.acquire()
#     pr_name = multiprocessing.current_process().name
#     print(f'Process {pr_name} started')
#     time.sleep(3)
#
#
# # i released another process from main and it finished "wrong"
# if __name__ == '__main__':
#     t1 = perf_counter()
#     lock = Lock()
#     pr1 = Process(target=get_value, args=(lock,)).start()
#     time.sleep(0.5)
#     lock.release()
#     pr2 = Process(target=get_value, args=(lock,)).start()
#     t2 = perf_counter()
#     print(f'Working time: {t2 - t1:.2f} seconds')

# # ------------------------------------------------------------------
# # RLOCK
# import multiprocessing
# import time
# from multiprocessing import Process, RLock
# from time import perf_counter
#
#
# def get_value(locked: RLock):
#     locked.acquire()
#     pr_name = multiprocessing.current_process().name
#     print(f'Process {pr_name} started')
#     time.sleep(3)
#
#
# # i tried to release this process from another(main) and get this err
# # AssertionError: attempt to release recursive lock not owned by thread
# if __name__ == '__main__':
#     t1 = perf_counter()
#     lock = RLock()
#     pr1 = Process(target=get_value, args=(lock,)).start()
#     time.sleep(0.5)
#     lock.release()
#     pr2 = Process(target=get_value, args=(lock,)).start()
#     t2 = perf_counter()
#     print(f'Working time: {t2 - t1:.2f} seconds')
# # that`s because it has been protected by RLock

# # ------------------------------------------------------------------
# ARRAY
import multiprocessing
import random
import time


def add_value(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        vtime = time.ctime()
        array[index] = num
        print(f'array[{index}] = {num}, time = [{vtime}]')
        time.sleep(num)


lock = multiprocessing.Lock()
arr = multiprocessing.Array('i', range(10))
processes = []

for i in range(10):
    pr = multiprocessing.Process(target=add_value, args=(lock, arr, i)).start()
    processes.append(pr)
