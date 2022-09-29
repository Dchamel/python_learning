class Critter(object):
    '''Virtual creature'''
    def __init__(self, name):
        print('New creature has been created')
        self.name = name
    def __str__(self):
        rep = 'Class object Critter\n'
        rep += f'Name: {self.name}\n'
        return rep
    def talk(self):
        print(f'Hello ! My name {self.name}')


crit = Critter('Doggy')
crit2 = Critter('Fishy')
crit.talk()
crit2.talk()
print(crit)

class Critter2(object):
    total = 0

    @staticmethod
    def status():
        print(f'Total Creatures: {Critter2.total}')

    def __init__(self, name):
        print('New creature has been created')
        self.name = name
        Critter2.total += 1

Critter2.status()
print(Critter2.total)
crit1 = Critter2('Chicken')
crit2 = Critter2('Chicken2')
print(crit2.total)
crit3 = Critter2('Chicken3')
Critter2.status()
print(crit2.total)