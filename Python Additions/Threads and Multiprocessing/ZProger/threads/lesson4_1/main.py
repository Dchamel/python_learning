import threading
import time

data = threading.local()


def get_name():
    print(data.name)


def t1():
    data.name = threading.currentThread().name
    time.sleep(100)


# def t2():
#     data.name = threading.currentThread().name
#     get_name()


threading.Thread(target=t1, name='t1').start()
# threading.Thread(target=t2, name='t2').start()
time.sleep(2)

# '_thread._local' object has no attribute 'name'
get_name()
