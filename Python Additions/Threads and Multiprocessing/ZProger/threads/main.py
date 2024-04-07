import threading
import time


def get_data(data):
    while True:
        print(f'{threading.current_thread().name} - {data}')
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),), name='thr-1')
thr.start()

for _ in range(20):
    print(f'current {_}')
    time.sleep(1)

    if _ % 10 == 0:
        print('active thread:', threading.active_count())
        print('enumerate:', threading.enumerate())
        print('thr-1 is alive', thr.is_alive())
        print(f'main thread: {threading.main_thread().name}')

print('name:', threading.main_thread().name)
threading.main_thread().name = 'абырвалГ'
# threading.main_thread().name = 'qwe123'
print('result:', threading.main_thread().name)

for _ in range(20):
    print(f'current {_}')
    time.sleep(1)

    if _ % 10 == 0:
        print('active thread:', threading.active_count())
        print('enumerate:', threading.enumerate())
        print('thr-1 is alive', thr.is_alive())
        print(f'main thread: {threading.main_thread().name}')
