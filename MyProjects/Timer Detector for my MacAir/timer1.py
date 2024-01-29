import time, keyboard
from datetime import datetime

i = 0
while True:
    if keyboard.is_pressed('escape'):
        print('exit')
        break
    else:
        time.sleep(1)
        i += 1
        dt = datetime.now()
        print(f'{i} - {dt.hour}:{dt.minute}:{dt.second}')


# print(time.time())