import multiprocessing
import time


# def t1():
#     for _ in range(3):
#         print(f'{multiprocessing.current_process().name} - {time.time()}')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     prcs = []
#     for _ in range(3):
#         pr = multiprocessing.Process(target=t1)
#         prcs.append(pr)
#         pr.start()
#     # print('Process started')
#     # time.sleep(5)
#     # pr.terminate()
#     # print(pr.is_alive())
#     # print(pr.pid)
#
#     for i in prcs:
#         i.join()

class Process(multiprocessing.Process):
    def run(self) -> None:
        print('work')


if __name__ == '__main__':
    pr = Process()
    pr.start()
