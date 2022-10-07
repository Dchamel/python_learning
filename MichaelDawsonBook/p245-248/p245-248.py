class Player(object):
    '''Player at the Action game'''
    def blast(self, enemy):
        print('Player shoots at the Enemy')
        enemy.die()

class Alien(object):
    '''Enemy at the Action game'''
    def die(self):
        print('Alien dying')

print('Stage of the Dying Alien')
hero = Player()
invader = Alien()
hero.blast(invader)
input('Press Enter for Exit')
