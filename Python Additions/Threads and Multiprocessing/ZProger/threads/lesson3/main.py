import threading
import time

value = 0

# main difference between Lock and RLock
# Lock can block and release thread from any thread
# RLock can be released only from locked thread
# locker = threading.Lock()
locker = threading.RLock()


def inc_value():
    global value
    while True:
        # we can use this two strings for locking and releasing thread
        # locker.acquire()
        # locker.release()
        # or context manager
        with locker:
            value += 1
            time.sleep(0.01)
            print(value, threading.current_thread().name)


for _ in range(5):
    threading.Thread(target=inc_value, name=f'Thread-{_}').start()
