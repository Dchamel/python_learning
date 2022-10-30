import unittest, random, games
from time import perf_counter
t1 = perf_counter()


print('Welcome to the Simple Game')
again = None
while again != 'n':
    players = []
    num = games.ask_number(question='How many Players in the Game ? (2-5):', low=2, high=5)

    for i in range(num):
        name = input('Your Name: ')
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)

    print('Game Results: ')
    for player in players:
        print(player)

    again = games.ask_yes_no('Again? (y/n): ')

input('Press Enter for Exit')


# Test Section
class AllTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Card(self):
        actual = ''
        self.assertEqual(actual, '')


t2 = perf_counter()
print(f'Main time: {t2 - t1:.5f} sec')
