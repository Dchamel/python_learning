class Critter(object):
    '''`Virtual Pet'''
    def __init__(self, name, mood):
        print('New pet has been created')
        self.name = name
        self.__mood = mood

    @property
    def mood(self):
        return self.__mood
    @mood.setter
    def mood(self, newMood):
        if newMood == '':
            print('Mood cant be Empty')
        else:
            self.__mood = newMood
            print('Mood has been changed.')

    def talk(self):
        print(f'My name is {self.name}')
        print(f'I feel myself {self.mood}\n')

    def __privateMethod(self):
        print('Private Method')

    def publicMethod(self):
        print('This is the Public Method')
        self.__privateMethod()

crit1 = Critter('Angie','Perfect')
print(crit1._Critter__mood) #direct access to private attributes
crit1.talk()
crit1.publicMethod()
crit1._Critter__privateMethod() # technical ability to call a private method. The same as with attributes upper
crit2 = Critter(mood = 'Nice', name = 'Lily')
crit2.talk()
crit2.mood = 'Funny'
crit2.talk()
print(crit2.name)
crit2.mood = ''

