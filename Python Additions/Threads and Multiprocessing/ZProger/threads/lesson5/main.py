# Semaphores
# import threading, time, random
#
# max_con = 5
#
#
# def t1(sem: threading.BoundedSemaphore) -> None:
#     """Simulates a working function with a specific working time"""
#     with sem:
#         work_time = random.randint(1, 5)
#         print(threading.current_thread().name, f'Working time:{work_time}')
#         time.sleep(work_time)
#
#
# if __name__ == '__main__':
#     sem = threading.BoundedSemaphore(value=max_con)
#     for i in range(10):
#         thr = threading.Thread(target=t1, args=(sem,)).start()
#
# --------------------------------------------

import time, random, threading


def t1(barrier) -> None:
    """qqq"""
    slp = random.randint(3, 17)
    time.sleep(slp)
    print(f'Thread[{threading.current_thread().name}] started at'
          f' {time.ctime()}')

    barrier.wait()
    print(f'Thread[{threading.current_thread().name}] goes trough '
          f'barrier at {time.ctime()}')


if __name__ == '__main__':
    bar = threading.Barrier(5)
    for i in range(5):
        threading.Thread(target=t1, args=(bar,)).start()
