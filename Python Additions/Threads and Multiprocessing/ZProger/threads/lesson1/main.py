import threading
import time


def get_data(data, val):
    for _ in range(val):
        print(f'{threading.current_thread().name} - {data}')
        time.sleep(1)


thr_list = []

for i in range(3):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f'thr-{i}')
    thr_list.append(thr)
    thr.start()

for i in thr_list:
    i.join()
