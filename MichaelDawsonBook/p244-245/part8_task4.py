class Critter(object):
    '''Virtual Pet Farm'''
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __passTime(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        data = f'Pet name: {self.name}, pet hunger: {self.hunger}, pet boredom: {self.boredom}'
        return  data

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = 'Cool'
        elif 5 <= unhappiness <= 10:
            mood = 'Good'
        elif 11 <= unhappiness <= 15:
            mood = 'Not so good'
        else:
            mood = 'Poor'
        return mood, unhappiness

    def talk(self):
        print(f'My name is {self.name}. And now i feel myself {self.mood}\n')
        self.__passTime()

    def eat(self, food = 4):
        food = int(input('How many time do you want to play: '))
        print('Thanks, User !')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__passTime()

    def play(self, fun = 4):
        fun = int(input('How many time do you want to play: '))
        print('Yaay !')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__passTime()


def chosenPet(crit):
    choice = None
    while choice != '0':
        print('''
        My Pet
        0 - Exit
        1 - Check Pet
        2 - Feed Pet
        3 - Play with Pet
        ''')
        choice = input('Your choice: ')

        #exit
        if choice == '0':
            print('Bye Master')
        #check
        elif choice == '1':
            crit.talk()
        #feed
        elif choice == '2':
            crit.eat()
        #play
        elif choice == '3':
            crit.play()
        elif choice == '4':
            print(crit)
        else:
            print('Sorry, wrong input.')

def main():
    choice = None
    petFarmDict = {}
    counter = 0
    while choice != '0':
        print('''
        My Pet Farm
        0 - Exit
        1 - Create New Pet
        2 - Play with Pets
        3 - Kill Pet
        ''')
        choice = input('Your choice: ')

        if choice == '1':
            critName = input('Give the name to your Pet: ')
            crit = Critter(critName)
            counter += 1
            petKeyforDict = f'Pet{counter}'
            petFarmDict[petKeyforDict] = crit
        elif choice == '2':
            choiceForPlay = None
            while choiceForPlay != '0':
                j = 1
                for i, pet in petFarmDict.items():
                    print(f'{j} - {i} - {pet.name}')
                    j += 1
                choiceForPlay = input('Your choice(0 - Exit): ')
                if choiceForPlay != '0':
                    chosenPet(petFarmDict[f'Pet{choiceForPlay}'])
            print(petFarmDict)
        elif choice == '3':
            choiceForKill = None
            while choiceForKill != '0':
                j = 1
                for i, pet in petFarmDict.items():
                    print(f'{j} - {i} - {pet.name}')
                    j += 1
                choiceForKill = input('Your choice(0 - Exit): ')
                if choiceForKill != '0':
                    del petFarmDict[f'Pet{choiceForKill}']

main()
input('Press Enter for exit...')
