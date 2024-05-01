import threading
import time


def get_data(data):
    for _ in range(5):
        print(f'{threading.current_thread().name} - {data}')
        time.sleep(1)


# first way to start daemon
thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True)
thr.start()
print('finish')

# another way to start daemon (deprecated - old way)
# thr = threading.Thread(target=get_data, args=(str(time.time()),))
# thr.setDaemon(True)
# thr.start()
# print('finish')
