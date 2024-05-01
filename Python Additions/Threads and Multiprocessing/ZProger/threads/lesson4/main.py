import threading
import time


def qtest():
    while True:
        print('Test')
        time.sleep(1)


thr = threading.Timer(5, qtest)
thr.setDaemon(True)  # deprecated
thr.start()

for _ in range(3):
    print('111')
    time.sleep(1)

# thr.cancel()
print('finish')
