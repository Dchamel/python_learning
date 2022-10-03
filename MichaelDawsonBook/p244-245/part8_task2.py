import keyboard

class Tv(object):
    '''Tv Control'''

    def chooseChannel(self, channel=1):
        channel = int(input('Input Channel number: '))
        self.channel = channel
        if self.channel < 1:
            self.channel = 1
        return channel

    def changeVolume(self, volume = 20):
        print('Press Up/Down Arrows on the Keyboard to\n'
              'increase or reduce Volume.')
        while True:
            if keyboard.is_pressed('up'):
                volume += 2
                print(f'Volume UP\nNow volume is {volume}')
            elif keyboard.is_pressed('down'):
                print('DOWN')
            elif keyboard.is_pressed('Escape'):
                print('Exit')
                break

q1 = Tv()
q1.changeVolume()