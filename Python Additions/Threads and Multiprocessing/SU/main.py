# import threading
# import time
#
#
# def thread_function(name):
#     print(name, ' - thread start')
#     time.sleep(2)
#     print(name, ' - thread finished')
#
#
# if __name__ == '__main__':
#     threads = []
#     for i in range(3):
#         print('creating thread: ', i)
#         x = threading.Thread(target=thread_function, args=(i,))
#         threads.append(x)
#         x.start()
#
#     for index, thread in enumerate(threads):
#         print('before joining thread: ', index)
#         thread.join()
#         print('after joining thread: ', index)

# # -------------------------------------------------------------------------------
#
# from concurrent.futures import ThreadPoolExecutor
# import threading, time
# from time import perf_counter
#
#
# def thread_function():
#     time.sleep(2)
#     print('thread_function finished {}'.format(threading.current_thread()))
#
#
# def main():
#     executor = ThreadPoolExecutor(max_workers=3)
#     task1 = executor.submit(thread_function)
#     task2 = executor.submit(thread_function)
#
#
# if __name__ == '__main__':
#     t1 = perf_counter()
#     main()
#     t2 = perf_counter()
#     print(f'elapsed time: {t2 - t1:.2f} sec')

# # -------------------------------------------------------------------------------
#
# import threading, time
# from queue import Queue
# from threading import Thread
# from time import perf_counter
#
# num_worker_threads = 2
#
#
# def do_work(item):
#     time.sleep(1)
#     print('my task is {}'.format(item), 'i`m', threading.current_thread())
#
#
# def worker():
#     while True:
#         item = q.get()
#         print('get task - {}'.format(item))
#         do_work(item)
#         q.task_done()
#
#
# def main():
#     for i in range(num_worker_threads):
#         t = Thread(target=worker)
#         t.setDaemon(True)
#         t.start()
#     for i in range(0, 5):
#         q.put(i)
#
#     q.join()
#
#
# if __name__ == '__main__':
#     t1 = perf_counter()
#     q = Queue()
#     main()
#     t2 = perf_counter()
#     print(f'elapsed time: {t2 - t1:.2f} sec')

# import threading
# import time
#
#
# def thread_function(name):
#     print(name, ' - thread start')
#     time.sleep(2)
#     print(name, ' - thread finished')
#
#
# if __name__ == '__main__':
#     threads = []
#     for i in range(3):
#         print('creating thread: ', i)
#         x = threading.Thread(target=thread_function, args=(i,))
#         threads.append(x)
#         x.start()
#
#     for index, thread in enumerate(threads):
#         print('before joining thread: ', index)
#         thread.join()
#         print('after joining thread: ', index)

# # -------------------------------------------------------------------------------
#
# from concurrent.futures import ThreadPoolExecutor
# import threading, time
# from time import perf_counter
#
#
# def thread_function():
#     time.sleep(2)
#     print('thread_function finished {}'.format(threading.current_thread()))
#
#
# def main():
#     executor = ThreadPoolExecutor(max_workers=3)
#     task1 = executor.submit(thread_function)
#     task2 = executor.submit(thread_function)
#
#
# if __name__ == '__main__':
#     t1 = perf_counter()
#     main()
#     t2 = perf_counter()
#     print(f'elapsed time: {t2 - t1:.2f} sec')

# # -------------------------------------------------------------------------------
#
# from multiprocessing import Process, current_process
#
#
# def foo(number):
#     proc_name = current_process().name
#     print('{0} {1}'.format(number, proc_name))
#
#
# if __name__ == '__main__':
#     random_numbers = [1, 2, 3, 4, 5]
#     process_list = []
#     proc = Process(target=foo, args=(5,))
#     for index, number in enumerate(random_numbers):
#         proc = Process(target=foo, args=(number,))
#         process_list.append(proc)
#         proc.start()
#     proc = Process(target=foo, name='Test', args=(11,))
#     proc.start()
#     process_list.append(proc)
#
#     for proc in process_list:
#         proc.join()

# # -------------------------------------------------------------------------------
#
# from multiprocessing import Process, Lock, current_process
# from time import perf_counter
#
#
# def pr_fun(item, lock):
#     lock.acquire()
#     try:
#         print(item, current_process())
#     finally:
#         lock.release()
#
#
# if __name__ == '__main__':
#     t1 = perf_counter()
#     lock = Lock()
#     items = ['test1', 'test2', 'test3']
#     for item in items:
#         p = Process(target=pr_fun, args=(item, lock))
#         p.start()
#     t2 = perf_counter()
#     print(f'Working time {t2 - t1:.2f} seconds')

# # -------------------------------------------------------------------------------
#
# from multiprocessing import Pool
# from time import perf_counter
#
#
# def calc(num):
#     return num * num
#
#
# if __name__ == '__main__':
#     numbers = [5, 10, 15, 20, 25, 30]
#     pool = Pool(processes=3)
#     print(pool.map(calc, numbers))

# # -------------------------------------------------------------------------------
#
# from multiprocessing import Process, Queue
# from time import perf_counter
#
# stop_number = -1
#
#
# def task_creator(data, q):
#     for item in data:
#         q.put(item)
#
#
# def consumer(q):
#     while True:
#         data = q.get()
#         print('data: {}'.format(data))
#         processed = data * 2
#         print(processed)
#         if data is stop_number:
#             break
#
#
# if __name__ == '__main__':
#     q = Queue()
#     data = [5, 10, 13, -1]
#     process_one = Process(target=task_creator, args=(data, q))
#     process_two = Process(target=consumer, args=(q,))
#     process_one.start()
#     process_two.start()
#     q.close()
#     q.join_thread()
#     process_one.join()
#     process_two.join()
