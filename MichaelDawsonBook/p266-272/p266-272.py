import unittest, random, cards, games
from time import perf_counter

t1 = perf_counter()

print('Welcome to the Black Jack game v1.0')


# from 1 to 7 Players can play


class BJ_Card(cards.Card):
    '''Card for Black Jack'''
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(cards.Deck):
    '''Deck for Black Jack'''

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    '''Hand with pack of cards for Black Jack'''

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + '\t' + super(BJ_Hand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cards:
            t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    pass


class BJ_Dealer(BJ_Hand):
    pass


class BJ_Game(object):
    pass


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
