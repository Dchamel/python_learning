import keyboard, time

class Tv(object):
    '''Tv Control'''

    def chooseChannel(self, channel=1):
        channel = int(input('Input Channel number: '))
        self.channel = channel
        if self.channel < 1:
            self.channel = 1
        elif self.channel > 100:
            self.channel = 100
        return channel

    def changeVolume(self, volume = 20):
        print('Press Up/Down Arrows on the Keyboard to\n'
              'increase or reduce Volume.')
        while True:
            if keyboard.is_pressed('up'):
                volume += 2
                time.sleep(0.1)
                print(f'Volume UP\nNow volume is {volume}')
                if volume > 98:
                    volume = 98
            elif keyboard.is_pressed('down'):
                volume -= 2
                time.sleep(0.1)
                print(f'Volume DOWN\nNow volume is {volume}')
                if volume < 2:
                    volume = 2
            elif keyboard.is_pressed('escape'):
                print('Exit')
                return volume

q1 = Tv()
userInput = ''
while userInput != '0':
    print('''
    Welcome to TV remote control
    0 - Exit
    1 - Change Channel
    2 - Change Volume''')
    userInput = input('Choice: ')
    if userInput == '1':
        print(f'You now at {q1.chooseChannel()} channel')
    elif userInput == '2':
        print(f'Volume of the Tv now is {q1.changeVolume()}')


