import unittest, random, cards
from time import perf_counter
t1 = perf_counter()

print('Welcome to the Black Jack v1.0')



class BJ_Card(cards.Card):
    pass

class BJ_Deck(cards.Deck):
    pass

class BJ_Hand(cards.Hand):
    pass

class BJ_Player(BJ_Hand):
    pass

class BJ_Dealer(BJ_Hand):
    pass

class BJ_Game(object):




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
